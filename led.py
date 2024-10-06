# LED class

import random

ADDRESS_RED = 8
ADDRESS_GREEN = ADDRESS_RED + 1
ADDRESS_BLUE = ADDRESS_RED  + 2

intensity_red = 0
intensity_green = 0
intensity_blue = 0

class Led():
    
    def __init__(self, address):
        self.address = address
        self.changeable = False
        self.counter = 1
        self.darker = True
        self.duration = 1
        self.initialized = False
        self.intensity = 0
        self.intensity_limit_max = 255
        self.intensity_limit_min = 1
        self.intensity_max = 255
        self.intensity_min = 1
        self.new_duration = True
        self.new_max_at_min = False
        self.new_min_at_max = False
        self.on = True
        self._is_at_max = False
        self._is_at_min = False
        self.wait_at_max = False
        self.wait_at_min = False
        
    def increase_intensity(self):
        self.intensity = self.intensity + 1
        if self.intensity >= self.intensity_max:
            self.darker = True
            self._is_at_max = True
            if self.new_duration == True:
                self.duration = 1 + int(random.random() * 7)
            if self.wait_at_max == True:
                self.changeable = False
            if self.new_min_at_max == True:
                value = int(random.random() * 255)
                if value < self.intensity and value >= self.intensity_limit_min:
                    self.intensity_min = value
        else:
            self._is_at_max = False
            self._is_at_min = False

    def decrease_intensity(self):
        self.intensity = self.intensity - 1
        if self.intensity <= self.intensity_min:
            self.darker = False
            self._is_at_min = True
            if self.new_duration == True:
                self.duration = 1 + int(random.random() * 7)
            if self.wait_at_min == True:
                self.changeable = False
            if self.new_max_at_min == True:
                value = int(random.random() * 255)
                if value > self.intensity and value <= self.intensity_limit_max:
                    self.intensity_max = value
        else:
            self._is_at_max = False
            self._is_at_min = False

    def change_intensity(self):
        if self.initialized == True:
            if self.changeable:
                self.counter = self.counter - 1
                if self.counter == 0:
                    self.counter = self.duration
                    if self.darker == True:
                        self.decrease_intensity()
                    else:
                        self.increase_intensity()
        else:
            if self.on == True:
                if self.intensity == self.intensity_limit_max:
                    self.initialized = True
                elif self.intensity <= self.intensity_limit_max:
                    self.intensity = self.intensity + 1
                else:
                    self.intensity = self.intensity - 1
            else:
                if self.intensity == self.intensity_limit_min:
                    self.initialized = True
                elif self.intensity >= self.intensity_limit_min:
                    self.intensity = self.intensity - 1
                else:
                    self.intensity = self.intensity + 1

class Rgb():

    def __init__(self, address_red, address_green, address_blue):
        self.list_leds = []
        self.list_leds.append(Led(address_red))
        self.list_leds.append(Led(address_green))
        self.list_leds.append(Led(address_blue))
        
    def logger(self):
        print("\nAdresses:")
        for i in self.list_leds:
            print(i.address)
        print("\nInitialized:")
        for i in self.list_leds:
            print(i.changeable)
        print("\nCounter:")
        for i in self.list_leds:
            print(i.counter)
        print("\nDarker:")
        for i in self.list_leds:
            print(i.darker)
        print("\nDuration:")
        for i in self.list_leds:
            print(i.duration)
        print("\nInitialized:")
        for i in self.list_leds:
            print(i.initialized)
        print("\nIntensity:")
        for i in self.list_leds:
            print(i.intensity)
        print("\nLimit max:")
        for i in self.list_leds:
            print(i.intensity_limit_max)
        print("\nLimit min:")
        for i in self.list_leds:
            print(i.intensity_limit_min)
        print("\nMax:")
        for i in self.list_leds:
            print(i.intensity_max)
        print("\nMin:")
        for i in self.list_leds:
            print(i.intensity_min)
        print("\nnew Duration:")
        for i in self.list_leds:
            print(i.new_duration)
        print("\nnew max at min:")
        for i in self.list_leds:
            print(i.new_max_at_min)
        print("\nnew min at max:")
        for i in self.list_leds:
            print(i.new_min_at_max)
        print("\nOn:")
        for i in self.list_leds:
            print(i.on)
        print("\nis at max:")
        for i in self.list_leds:
            print(i._is_at_max)
        print("\nis at min:")
        for i in self.list_leds:
            print(i._is_at_min)
        print("\nwait at max:")
        for i in self.list_leds:
            print(i.wait_at_max)
        print("\nwait at min:")
        for i in self.list_leds:
            print(i.wait_at_min)

