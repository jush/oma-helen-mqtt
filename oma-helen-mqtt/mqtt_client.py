from helenservice.price_client import HelenPriceClient
from helenservice.api_client import HelenApiClient
from paho.mqtt import client as paho
import json

class HelenMqttClient:
    tax = 0.1 # 10%
    helen_price_client = HelenPriceClient()
    # initial margin
    margin = helen_price_client.get_exchange_prices().margin
    api_client = HelenApiClient(tax, margin)
    mqtt_client = paho.Client(client_id="", userdata=None, protocol=paho.MQTTv5)

    def __init__(self, mqtt_hostname = None, mqtt_port=None, mqtt_username = None, mqtt_password = None):
        self._mqtt_hostname = "127.0.0.1" if mqtt_hostname is None or mqtt_hostname == "" else mqtt_hostname
        self._mqtt_port = 1883 if mqtt_port is None or mqtt_port == "" else mqtt_port
        self.mqtt_client.username_pw_set(mqtt_username, mqtt_password)
        self.mqtt_client.connect(host=self._mqtt_hostname, port=self._mqtt_port)
        self.mqtt_client.publish("oma_helen/state", payload=json.dumps({ "margin": self.margin, "tax": self.tax }))