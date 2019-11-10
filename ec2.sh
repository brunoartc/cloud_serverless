#!/bin/bash
cd /home/ubuntu
git clone https://github.com/brunoartc/cloud_serverless
cd cloud_serverless
sudo apt-get install software-properties-common
sudo apt-add-repository universe
sudo apt-get update -y
sudo apt-get install python-pip openvpn -y
sudo apt install python3-pip -y
pip3 install -r requirments.txt
tmux new -d -s todo 'export SERVER="http://10.8.0.10";python3 main.py;' 