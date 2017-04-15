#!/usr/bin/env python
# -*- coding: utf-8 -*-

import kivy
kivy.require('1.9.1')

from kivy.app import App
from kivy.clock import Clock
from kivy.properties import ObjectProperty
from kivy.uix.boxlayout import BoxLayout
from kivy.core.window import Window
from kivy.core.text import LabelBase
from kivy.utils import get_color_from_hex

from time import strftime

__author__ = "Icaro Perseo"
__copyright__ = "Icaro Perseo"
__license__ = "gpl3"


class ClockUI(BoxLayout):
    stopwatch_property = ObjectProperty(None)
    start_stop_property = ObjectProperty(None)
    time_property = ObjectProperty(None)


class ClockApp(App):
    sw_seconds = 0
    sw_started = False

    def build(self):
        self.icon = 'assets/img/icon.png'
        self.title = 'kvClock'

        return ClockUI()

    def on_start(self):
        Clock.schedule_interval(self.update, 0)

    def update(self, nap):
        if self.sw_started:
            self.sw_seconds += nap

        self.root.time_property.text = strftime('[b]%H[/b]:%M:%S')

        minutes, seconds = divmod(self.sw_seconds, 60)
        self.root.stopwatch_property.text = ('%02d:%02d.[size=40]%02d[/size]' % (int(minutes),
                                                                                 int(seconds),
                                                                                 int(seconds * 100 % 100)))

    def start_stop(self):
        self.root.start_stop_property.text = ('Start' if self.sw_started else 'Stop')
        self.sw_started = not self.sw_started

    def reset(self):
        if self.sw_started:
            self.root.start_stop_property.text = 'Start'
            self.sw_started = False

        self.sw_seconds = 0

if __name__ == '__main__':
    Window.clearcolor = get_color_from_hex('#101216')
    Window.size = (360, 280)
    LabelBase.register(name='Roboto',
                       fn_regular='assets/fonts/Roboto-Thin.ttf',
                       fn_bold='assets/fonts/Roboto-Medium.ttf')
    ClockApp().run()
