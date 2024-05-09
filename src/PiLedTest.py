from hal import hal_input_switch as switch
from hal import hal_led as led
import time
from time import sleep

def main():
    count = 0
    i = 1
    while i == 1:
        switch.init()
        led.init()
    

        switchLevel = switch.read_slide_switch()
        while switchLevel == 1:
            count = 0
            led.set_output(0,1)
            time.sleep(1)
            led.set_output(0,0)
            time.sleep(1)
            switchLevel = switch.read_slide_switch()

        while switchLevel == 0:
            while count < 6:
                led.set_output(0,1)
                time.sleep(0.5)
                led.set_output(0,0)
                time.sleep(0.5)
                switchLevel = switch.read_slide_switch()
                count = count + 1

            led.set_output(0,0)
            switchLevel = switch.read_slide_switch()


        





if __name__ =="__main__":
    main()
