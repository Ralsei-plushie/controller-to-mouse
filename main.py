import pyglet
from pyglet.input import ControllerManager
import sys
import pyautogui as pyui
import time

man = ControllerManager()

pyui.PAUSE = 0
control = man.get_controllers()
control2 = control[0]
control2.open()

class ControlPython:
    def on_dpad_motion(self, controller, value):
        global moveright, moveup, moveleft, movedown
        moveright = (value.x == 1)
        moveup = (value.y == 1)
        moveleft = (value.x == -1)
        movedown = (value.y == -1)
    def update(self, dt):
        if moveright:
            pyui.moveRel(15, 0)
        if moveup:
            pyui.moveRel(0, -15)
        if moveleft:
            pyui.moveRel(-15, 0)
        if movedown:
            pyui.moveRel(0, 15)
            
    def on_button_press(self, controller, button_name):
        if button_name == "rightshoulder":
            pyui.click()
        if button_name == "leftshoulder":
            pyui.leftClick()


hand = ControlPython()
control2.push_handlers(hand)

pyglet.clock.schedule_interval(hand.update, 0.05)
pyglet.app.run()
