sudo chmod a+rw /dev/ttyUSB0
sudo chmod a+rw /dev/ttyUSB1

docker run --rm -it -v /tmp/.X11-unix:/tmp/.X11-unix -v $(pwd):/app -e DISPLAY=$DISPLAY -u qtuser -p 12346:12345 --device /dev/ttyUSB0:/dev/ttyUSB0 pneumo python3 press_app_qt/app_x/main.py
docker run --rm -it -v /tmp/.X11-unix:/tmp/.X11-unix -v $(pwd):/app -e DISPLAY=$DISPLAY -u qtuser -p 12346:12345 --device /dev/ttyUSB1:/dev/ttyUSB0 pneumo python3 press_app_qt/app_x/main.py