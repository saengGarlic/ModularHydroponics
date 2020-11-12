
'''

class controlmodel:
    #1 manual mode
        scheduling option

    #2 thresold model
        target value를 경계로 동작 정의

    #3 linear model


'''

from threading import Thread
import time


class Controlmodel:
    def linearcon(self, **kwargs):
        wantdata = kwargs.pop('wantdata', None)
        sensingdata = kwargs.pop('sensingdata', None)
        actufunc = kwargs.pop('actufunc', None)
        actumeta = kwargs.pop('actumeta', None)
        global flag
        flag = 0
        if flag == 1:
            if wantdata + 0.1 >= sensingdata >= wantdata - 0.1:
                flag = 0
                pass
            elif wantdata + 0.1 < sensingdata:
                print("Pump2 on()")
                ## bus.write_byte(address, 3) actu minus
            elif sensingdata < wantdata - 0.1:
                print("Pump1 on()")
                ## bus.write_byte(address, 2) actu plus
            else:
                pass
        elif flag == 0:
            if sensingdata < wantdata - 0.5:
                print("Pump1 on()")
                ## bus.write_byte(address, 2) actu minus
                flag = 1
            elif sensingdata > wantdata + 0.5:
                print("Pump2 on()")
                ## bus.write_byte(address, 3) actu plus
                flag = 1
            elif wantdata - 0.5 <= sensingdata <= wantdata + 0.5:
                pass
            else:
                pass
        else:
            pass

    def thresoldcon(self, **kwargs):
        wantdata = kwargs.pop('wantdata', None)
        sensingdata = kwargs.pop('sensingdata', None)
        actuator = kwargs.pop('actuator', None)
        if sensingdata > wantdata:
            print("LED off()")## bus.write_byte(address, 3)
        elif sensingdata <= wantdata:
            print("LED on()")## bus.write_byte(address, 2)
        else:
            pass