from getpass import getpass
from .mqtt_client import HelenMqttClient

def main():
    print("Log in to Oma Helen")
    oma_helen_username = input("Oma Helen username: ")
    oma_helen_password = getpass("Oma Helen password: ")
    mqtt_host = input("MQTT host: ")
    mqtt_username = input("MQTT username: ")
    mqtt_password = getpass("MQTT password: ")

    HelenMqttClient(mqtt_hostname=mqtt_host)
    


if __name__ == "__main__":
    main()