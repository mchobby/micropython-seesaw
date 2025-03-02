mpremote fs mkdir :lib/seesaw
mpremote fs cp lib/seesaw/*.py :lib/seesaw/

# adafruit_pixelbuf
wget https://raw.githubusercontent.com/adafruit/Adafruit_CircuitPython_Pixelbuf/refs/heads/main/adafruit_pixelbuf.py -O lib/adafruit_pixelbuf.py
mpremote fs cp lib/adafruit_pixelbuf.py :lib/
