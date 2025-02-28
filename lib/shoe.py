#!/usr/bin/env python3

class Shoe:
    def __init__(self, brand, size):
        self._brand = brand
        self._size = size
        self.condition = 'Old'
        
    @property
    def brand(self):
        return self._brand
    
    @brand.setter
    def brand(self, brand):
        if isinstance(brand, str):
            self._brand = brand

    @property
    def size(self):
        return self._size
    
    @size.setter
    def size(self, size):
        if isinstance(size, int):
            self._size = size
        else:
            print("size must be an integer")

    def cobble(self):
        print('Your shoe is as good as new!')
        self.condition = 'New'
        # condition = 'New'