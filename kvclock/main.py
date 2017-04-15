#!/usr/bin/env python
# -*- coding: utf-8 -*-

import kivy
kivy.require('1.9.1')

from kivy.app import App
from kivy.clock import Clock
from kivy.uix.boxlayout import BoxLayout
from kivy.core.window import Window
from kivy.core.text import LabelBase
from kivy.utils import get_color_from_hex

from time import strftime

__author__ = "Icaro Perseo"
__copyright__ = "Icaro Perseo"
__license__ = "gpl3"


class ClockUI(BoxLayout):
    pass


class ClockApp(App):
    icon = 'assets/img/icon.png'
    title = 'kvClock'

    def build(self):
        return ClockUI()

    def on_start(self):
        Clock.schedule_interval(self.update, 0)

    def update(self, nap):
        self.root.ids.time.text = strftime('[b]%H[/b]:%M:%S')

if __name__ == '__main__':
    Window.clearcolor = get_color_from_hex('#101216')
    Window.size = (360, 280)
    LabelBase.register(name='Roboto',
                       fn_regular='assets/fonts/Roboto-Thin.ttf',
                       fn_bold='assets/fonts/Roboto-Medium.ttf')
    ClockApp().run()
