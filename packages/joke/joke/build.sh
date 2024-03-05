#!/bin/bash

set -e

virtualenv --without-pip virtualenv
pip3 install -r requirements.txt --target virtualenv/lib/python3.9/site-packages
