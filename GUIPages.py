from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.core.window import Window
Window.size = (480, 320)
# Create both screens. Please note the root.manager.current: this is how
# you can control the ScreenManager from kv. Each screen has by default a
# property manager that gives you the instance of the ScreenManager used.
Builder.load_file('slider2.kv')

numberList = []
textInput = 0
# Declare both screens
class FadersScreenA(Screen):
    def slide_it_red(self, *args):
        print(args[1])

    def slide_it_green(self, *args):
        print(args[1])

    def slide_it_blue(self, *args):
        print(args[1])

    pass

class FadersScreenB(Screen):
    def slide_it_red(self, *args):
        print(args[1])

    def slide_it_green(self, *args):
        print(args[1])

    def slide_it_blue(self, *args):
        print(args[1])

    pass

class FadersScreenC(Screen):
    def slide_it_red(self, *args):
        print(args[1])

    def slide_it_green(self, *args):
        print(args[1])

    def slide_it_blue(self, *args):
        print(args[1])

    pass

class ColorGroups(Screen):

    pass

class NumberPadScreen(Screen):
    pass

    def appendNumber(self, instance):
        pass

    def fixChannels(self, instance):
        global textInput
        textInput = 0

    def fixLow(self, instance):
        global textInput
        textInput = 1

    def fixHigh(self, instance):
        global textInput
        textInput = 2

    def buttonPress(self, button):
        global prior
        if textInput == 0:
            prior = self.ids.fixChannels.text
            if prior == 'Channels per Fixture':
                self.ids.fixChannels.text = ''
                self.ids.fixChannels.text = f'{button}'
            else:
                self.ids.fixChannels.text = f'{prior}{button}'
        if textInput == 1:
            prior = self.ids.fixLow.text
            if prior == 'Fixture # Low':
                self.ids.fixLow.text = ''
                self.ids.fixLow.text = f'{button}'
            else:
                self.ids.fixLow.text = f'{prior}{button}'
        if textInput == 2:
            prior = self.ids.fixHigh.text
            if prior == 'Fixture # High':
                self.ids.fixHigh.text = ''
                self.ids.fixHigh.text = f'{button}'
            else:
                self.ids.fixHigh.text = f'{prior}{button}'

    def clear(self, instance):
        if textInput == 0:
            self.ids.fixChannels.text = 'Channels per Fixture'
        if textInput == 1:
            self.ids.fixLow.text = 'Fixture # Low'
        if textInput == 2:
            self.ids.fixHigh.text = 'Fixture # High'
        pass

    def delete(self, instance):
        global prior
        if textInput == 0:
            prior = self.ids.fixChannels.text
            self.ids.fixChannels.text = prior[0:len(prior)-1]
        if textInput == 1:
            prior = self.ids.fixLow.text
            self.ids.fixLow.text = prior[0:len(prior)-1]
        if textInput == 2:
            prior = self.ids.fixHigh.text
            self.ids.fixHigh.text = prior[0:len(prior)-1]

class SettingsScreen(Screen):

    pass



class TestApp(App):

    def build(self):
        # Create the screen manager
        sm = ScreenManager()
        sm.add_widget(FadersScreenA(name='fadersA'))
        sm.add_widget(FadersScreenB(name='fadersB'))
        sm.add_widget(FadersScreenC(name='fadersC'))
        sm.add_widget(ColorGroups(name='Color Groups'))
        sm.add_widget(NumberPadScreen(name='numbers'))
        sm.add_widget(SettingsScreen(name='settings'))

        return sm

if __name__ == '__main__':
    TestApp().run()
