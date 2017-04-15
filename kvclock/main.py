#!/usr/bin/env python
# -*- coding: utf-8 -*-

import kivy
kivy.require('1.9.1')

from kivy.app import App
from kivy.uix.widget import Widget

__author__ = "Icaro Perseo"
__copyright__ = "Icaro Perseo"
__license__ = "gpl3"


class Clock(Widget):
    pass


class ClockApp(App):
    def build(self):
        return Clock()

if __name__ == '__main__':
    ClockApp().run()
