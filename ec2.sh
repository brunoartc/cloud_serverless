#!/bin/bash
cd ~
git clone https://github.com/brunoartc/cloud_serverless
cd cloud_serverless
pip3 install -r requirments.txt
python3 main.py