import serial
from serial.serialutil import SerialException
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.slider import Slider
from kivy.uix.button import Button
from kivy.uix.popup import Popup
from kivy.uix.colorpicker import ColorPicker

class LightingConsoleApp(App):
    def build(self):
        self.effects = ["Effect 1", "Effect 2", "Effect 3"]
        self.port = '/dev/tty.usbmodem113101'
        try:
            self.ser = serial.Serial(self.port, 9600)
        except SerialException:
            print("Could not open serial connection. Please connect the Arduino.")
            self.ser = None

        self.root = BoxLayout(orientation='horizontal')

        for i in range(1, 6):
            box = BoxLayout(orientation='vertical')
            label = Label(text='Channel '+str(i))
            box.add_widget(label)
            slider = Slider(min=0, max=255, orientation='vertical')
            slider.bind(value=lambda instance, value, channel=i: self.change_dmx_value(channel, value))
            box.add_widget(slider)
            button = Button(text='Color')
            button.bind(on_release=lambda instance, slider=slider: self.open_color_picker(slider))
            box.add_widget(button)
            self.root.add_widget(box)

        effect_box = BoxLayout(orientation='vertical')
        for effect in self.effects:
            button = Button(text=effect)
            button.bind(on_release=lambda instance, effect=effect: self.trigger_effect(effect))  
            effect_box.add_widget(button)
        self.root.add_widget(effect_box)

        return self.root

    def change_dmx_value(self, channel, value):
        if self.ser is not None:
            self.ser.write(bytes([channel, int(value)]))

    def trigger_effect(self, effect):
        if self.ser is not None:
            self.ser.write(bytes([0, self.effects.index(effect) + 1]))

    def open_color_picker(self, slider):
        color_picker = ColorPicker()
        apply_button = Button(text="Apply", size_hint=(1, 0.1))
        popup_content = BoxLayout(orientation='vertical')
        popup_content.add_widget(color_picker)
        popup_content.add_widget(apply_button)
        popup = Popup(title="Pick a color", content=popup_content)

        apply_button.bind(on_release=lambda instance: self.set_slider_color(color_picker.color, slider, popup))
        popup.open()

    def set_slider_color(self, color, slider, popup):
        slider.background_color = color
        popup.dismiss()

LightingConsoleApp().run()

