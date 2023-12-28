#!/usr/bin/env python

"""The setup script."""

import pathlib
from setuptools import setup, find_packages

here = pathlib.Path(__file__).parent.resolve()
long_description = (here / "README.md").read_text(encoding="utf-8")

requirements = [
    'oma-helen-cli>=1.1.1',
    'paho-mqtt>=1.6.1',
    ]

setup(
    author="jush",
    author_email='oni.pool@gmail.com',
    python_requires='>=3.6',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Intended Audience :: End Users/Desktop',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ],
    description="Oma Helen API exposed as MQTT",
    entry_points={
        'console_scripts': [
            'oma-helen-mqtt=oma-helen-mqtt.cli:main',
        ],
    },
    name="oma-helen-mqtt",
    install_requires=requirements,
    license="MIT license",
    long_description=long_description,
    long_description_content_type='text/markdown',
    packages=find_packages(include=['oma-helen-mqtt', 'oma-helen-mqtt.*']),
    url='https://github.com/jush/oma-helen-mqtt',
    version='0.1',
)