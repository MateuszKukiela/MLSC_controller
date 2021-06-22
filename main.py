import requests
import time
from pigpio_encoder.rotary import Rotary

URL = 'http://raspberrypi:8080/SetActiveEffectForAll'


def rotary_callback(counter):
    print("Counter value: ", URL)
    # return


def sw_short():
    # print("Switch short press")
    return


my_rotary = Rotary(
  clk_gpio=27,
  dt_gpio=22,
  sw_gpio=17
)
my_rotary.setup_rotary(
  min=0,
  max=300,
  scale=1,
  debounce=200,
  rotary_callback=rotary_callback
)
my_rotary.setup_switch(
  debounce=200,
  long_press=True,
  sw_short_callback=sw_short,
)

if __name__ == '__main__':
    requests.post(URL, json={"effect": "effect_single"})
    time.sleep(1)
    requests.post(URL, json={"effect": "effect_off"})
    time.sleep(1)
    # while True:
    #     key = input()
    #     if key == 'w':
    #         print('dupa')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
