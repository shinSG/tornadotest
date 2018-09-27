#!/usr/bin/python
# encoding: utf-8


class Test(object):
    def __init__(self):
        self.flag = 1
        
    def a(self):
        print id(self)
        self.flag += 1
        print self.flag
