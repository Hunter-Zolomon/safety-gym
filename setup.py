#!/usr/bin/env python

from setuptools import setup, find_packages
import sys

assert sys.version_info.major == 3 and sys.version_info.minor >= 6, \
    "Safety Gym is designed to work with Python 3.6 and greater. " \
    + "Please install it before proceeding."

setup(
    name='safety_gym',
    version='0.1',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'gym~=0.19.0',
        'joblib~=1.0.1',
        'mujoco_py',
        'numpy~=1.21.6',
        'xmltodict~=0.12.0',
    ],
)
