#!/bin/bash
while :
do
        python3 randomart.py
        python3 mastodon_images.py
        python3 resize_image.py
        sleep 300
done
