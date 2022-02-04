from __future__ import print_function
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.uix.button import Button
from kivy.uix.slider import Slider
from kivy.uix.textinput import TextInput
from kivy.config import Config
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.core.window import Window
from kivy.clock import Clock
from kivy.lang import Builder
from kivy.uix.slider import Slider
from DMXEnttecPro import Controller
import time

dmx = Controller('/dev/cu.usbserial-EN259682')  # Typical of Linux
#dmx = Controller('/dev/cu.usbserial-AL05O8ZE')  # Typical of Linux

Window.size = (1720, 1080)
channelLow = 1
channelHigh = 1
fixture = 0
red = 0
green = 0
blue = 0
save = 0
play = 0
sCue = 0
sCueRecord = 0
c = 0
colorSave = 0
color = 0
channelLow = '0'
channelHigh = '0'

compensation = 0.0004
tempo = 186
timing = 15/tempo
beat_length = 15/tempo - compensation
next_beat = time.time() + beat_length
timeList = []
s = 0
average = 0
beat = 0


color1 = (0,0,0)
color2 = (0,0,0)
color3 = (0,0,0)
color4 = (0,0,0)

colorList = [color1, color2, color3, color4]

Builder.load_file('sliderR.kv')

numberOfFixtures = 0
channelsPerFixture = 3
cue = 0

cueList1 = [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0],
            [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]]

cueList2 = [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0],
            [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]]

cueList3 = [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0],
            [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]]

cueList4 = [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0],
            [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]]

cueList5 = [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0],
            [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]]

cueList6 = [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0],
            [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]]

cueList7 = [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0],
            [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]]

cueList8 = [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0],
            [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]]

allCuesList = [cueList1, cueList2, cueList3, cueList4, cueList5, cueList6, cueList7, cueList8]

superCue1 = []
superCue2 = []
superCue3 = []
superCue4 = []

superCueList = [superCue1, superCue2, superCue3, superCue4]


# def superCueRecording():
#     global x
#     x = 0
#     for i in superCueList:
#         if sCueRecord % 2 == 1 and sCue == x:
#             superCueList[x].append(cue)
#             if superCueList[x][0] == 10:
#                 superCueList[x].pop(0)
#         x += 1

class MyLayout(GridLayout):
    def __init__(self, **kwargs):
        global x
        global z
        super(MyLayout, self).__init__(**kwargs)

        self.cols = 1
        self.z = 40


        self.textGrid = GridLayout()
        self.textGrid.cols = 4
        self.textGrid.padding = 4
        self.textGrid.spacing = 2
        self.textGrid.size_hint_y = 0
        self.add_widget(self.textGrid)

        self.red = TextInput(multiline=False, font_size=20)
        #self.textGrid.add_widget(self.red)

        self.green = TextInput(multiline=False, font_size=20)
        #self.textGrid.add_widget(self.green)

        self.blue = TextInput(multiline=False, font_size=20)
        #self.textGrid.add_widget(self.blue)

        self.colorGrid = GridLayout()
        self.colorGrid.cols = 9
        self.colorGrid.padding = 4
        self.colorGrid.spacing = 2
        self.colorGrid.size_hint_y = .4
        self.add_widget(self.colorGrid)

        self.colorSaveButton = Button(text='Save Color', background_color='gray', size_hint_x=0.1, size_hint_y=0.1)
        self.colorGrid.add_widget(self.colorSaveButton)
        self.colorSaveButton.bind(on_press=self.colorSave)

        self.color1Button = Button(text='Color 1', background_color='gray', background_normal= '', size_hint_x=0.1, size_hint_y=0.1)
        self.colorGrid.add_widget(self.color1Button)
        self.color1Button.bind(on_press=self.color1)

        self.color2Button = Button(text='Color 2', background_color='gray', background_normal= '', size_hint_x=0.1, size_hint_y=0.1)
        self.colorGrid.add_widget(self.color2Button)
        self.color2Button.bind(on_press=self.color2)

        self.color3Button = Button(text='Color 3', background_color='gray', background_normal='', size_hint_x=0.1, size_hint_y=0.1)
        self.colorGrid.add_widget(self.color3Button)
        self.color3Button.bind(on_press=self.color3)

        self.color4Button = Button(text='Color 4', background_color='gray', background_normal='', size_hint_x=0.1, size_hint_y=0.1)
        self.colorGrid.add_widget(self.color4Button)
        self.color4Button.bind(on_press=self.color4)

        # self.transportGrid = GridLayout()
        # self.transportGrid.cols = 4
        # self.transportGrid.padding = 4
        # self.transportGrid.spacing = 2
        # self.transportGrid.size_hint_y = .7
        # self.add_widget(self.transportGrid)
        #
        # self.playButton = Button(text='Play', background_color='gray', size_hint_x=0.1, size_hint_y=0.1)
        # self.transportGrid.add_widget(self.playButton)
        # self.playButton.bind(on_press=self.play)
        #
        # self.stopButton = Button(text='Stop', background_color='gray', size_hint_x=0.1, size_hint_y=0.1)
        # self.transportGrid.add_widget(self.stopButton)
        # self.stopButton.bind(on_press=self.stop)

        # self.channelGrid = GridLayout()
        # self.channelGrid.cols = 4
        # self.channelGrid.padding = 4
        # self.channelGrid.spacing = 2
        # self.channelGrid.size_hint_y = .4
        # self.add_widget(self.channelGrid)
        #
        # self.setChannelButton = Button(text='Set Channel', background_color='gray', size_hint_x=0.1, size_hint_y=0.1)
        # self.channelGrid.add_widget(self.setChannelButton)
        # self.setChannelButton.bind(on_press=self.setChannel)
        #
        # # self.saveButton = Button(text='Save', background_color='gray', size_hint_x=0.1, size_hint_y=0.1)
        # # self.channelGrid.add_widget(self.saveButton)
        # # self.saveButton.bind(on_press=self.save)
        #
        # self.channelLow = TextInput(multiline=False, font_size=44, size_hint_x=0.1, size_hint_y=0.1)
        # self.channelGrid.add_widget(self.channelLow )
        #
        # self.channelHigh = TextInput(multiline=False, font_size=44, size_hint_x=0.1, size_hint_y=0.1)
        # self.channelGrid.add_widget(self.channelHigh)

        self.cueGrid = GridLayout()
        self.cueGrid.cols = 4
        self.cueGrid.padding = 4
        self.cueGrid.spacing = 2
        self.cueGrid.size_hint_y = .4
        self.add_widget(self.cueGrid)


        self.cue1Button = Button(text='Cue 1', background_color='gray', size_hint_x=0.1, size_hint_y=0.1)
        self.cueGrid.add_widget(self.cue1Button)
        self.cue1Button.bind(on_press=self.cue1)

        self.cue2Button = Button(text='Cue 2', background_color='gray', size_hint_x=0.1, size_hint_y=0.1)
        self.cueGrid.add_widget(self.cue2Button)
        self.cue2Button.bind(on_press=self.cue2)

        self.cue3Button = Button(text='Cue 3', background_color='gray', size_hint_x=0.1, size_hint_y=0.1)
        self.cueGrid.add_widget(self.cue3Button)
        self.cue3Button.bind(on_press=self.cue3)

        self.cue4Button = Button(text='Cue 4', background_color='gray', size_hint_x=0.1, size_hint_y=0.1)
        self.cueGrid.add_widget(self.cue4Button)
        self.cue4Button.bind(on_press=self.cue4)

        self.cueGrid2 = GridLayout()
        self.cueGrid2.cols = 4
        self.cueGrid2.padding = 4
        self.cueGrid2.spacing = 2
        self.cueGrid2.size_hint_y = .4
        self.add_widget(self.cueGrid2)

        self.cue5Button = Button(text='Cue 5', background_color='gray', size_hint_x=0.1, size_hint_y=0.1)
        self.cueGrid2.add_widget(self.cue5Button)
        self.cue5Button.bind(on_press=self.cue5)

        self.cue6Button = Button(text='Cue 6', background_color='gray', size_hint_x=0.1, size_hint_y=0.1)
        self.cueGrid2.add_widget(self.cue6Button)
        self.cue6Button.bind(on_press=self.cue6)

        self.cue7Button = Button(text='Cue 7', background_color='gray', size_hint_x=0.1, size_hint_y=0.1)
        self.cueGrid2.add_widget(self.cue7Button)
        self.cue7Button.bind(on_press=self.cue7)

        self.cue8Button = Button(text='Cue 8', background_color='gray', size_hint_x=0.1, size_hint_y=0.1)
        self.cueGrid2.add_widget(self.cue8Button)
        self.cue8Button.bind(on_press=self.cue8)

        self.color1(self)

        self.timing(self)

    # def play(self, instance):
    #     global play
    #     global p
    #     global cue
    #     global c
    #     global beat
    #     play += 1
    #     beat += 1
    #     c = 0
    #     time.sleep(beat_length)
    #
    #
    #
    # def stop(self, instance):
    #     global play
    #     global p
    #     global beat
    #     play = 0
    #     beat = 0

    def setChannel(self, instance):
        global channelLow
        global channelHigh
        global fixture
        global save

        channelLow = self.ids.fixLow.text
        channelHigh = self.ids.fixHigh.text
        save += 1


    # def save(self, instance):
    #     global channelLow
    #     global channelHigh
    #     global fixture
    #     global save
    #
    #     save = 0

    def colorSave(self, instance):
        global colorSave
        colorSave += 1
        self.colorSaveButton.background_color = 'red'

    def color1(self, instance):
        global colorSave
        global color
        color = 0
        colorSave = 0
        self.red.text = str(colorList[color][0])
        self.green.text = str(colorList[color][1])
        self.blue.text = str(colorList[color][2])

    def color2(self, instance):
        global colorSave
        global color
        color = 1
        colorSave = 0
        self.red.text = str(colorList[color][0])
        self.green.text = str(colorList[color][1])
        self.blue.text = str(colorList[color][2])

    def color3(self, instance):
        global colorSave
        global color
        color = 2
        colorSave = 0
        self.red.text = str(colorList[color][0])
        self.green.text = str(colorList[color][1])
        self.blue.text = str(colorList[color][2])

    def color4(self, instance):
        global colorSave
        global color
        color = 3
        colorSave = 0
        self.red.text = str(colorList[color][0])
        self.green.text = str(colorList[color][1])
        self.blue.text = str(colorList[color][2])


    def channelLow(self, instance):
        print(1)

    def channelHigh(self, instance):
        print(1)

    def cue1(self, instance):
        global cue
        cue = 0
        # superCueRecording()

    def cue2(self, instance):
        global cue
        cue = 1
        #superCueRecording()

    def cue3(self, instance):
        global cue
        cue = 2
       # superCueRecording()

    def cue4(self, instance):
        global cue
        cue = 3
        #superCueRecording()

    def cue5(self, instance):
        global cue
        cue = 4
       # superCueRecording()

    def cue6(self, instance):
        global cue
        cue = 5
        #superCueRecording()

    def cue7(self, instance):
        global cue
        cue = 6
        #superCueRecording()

    def cue8(self, instance):
        global cue
        cue = 7
       # superCueRecording()

    # def superCueRecord(self, instance):
    #     global sCueRecord
    #     sCueRecord += 1
    #
    # def superCueClear(self, instance):
    #     global sCue
    #     superCueList[sCue].clear()
    #
    # def superCue1(self, instance):
    #     global sCue
    #     sCue = 0
    #
    # def superCue2(self, instance):
    #     global sCue
    #     sCue = 1
    #
    # def superCue3(self, instance):
    #     global sCue
    #     sCue = 2
    #
    # def superCue4(self, instance):
    #     global sCue
    #     sCue = 3

    def slide_it_red(self, *args):
        self.red.text = str(int(args[1]))

    def slide_it_green(self, *args):
        self.green.text = str(int(args[1]))

    def slide_it_blue(self, *args):
        self.blue.text = str(int(args[1]))

    def color8(self, instance):
        global Gcolor
        global Bcolor
        global Rcolor
        global save
        global color8

        if save == 1:
            color8 = (Rcolor, Gcolor, Bcolor)
            self.color8Button.background_color = (Rcolor / 255, Gcolor / 255, Bcolor / 255)
            self.saveButton.background_color = 'gray'
            save = 0
        if save == 0:
            self.RGBinputRed.text = str(int(color8[0]))
            self.RGBinputGreen.text = str(int(color8[1]))
            self.RGBinputBlue.text = str(int(color8[2]))

    def appendNumber(self, instance):
        pass


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


    def timing(self, instance):
        global channelLow
        global channelHigh
        global dmxNumber
        global red
        global green
        global blue
        global fixture
        global save
        global cue
        global x
        global sCue
        global colorSave
        global red
        global green
        global blue
        global color1
        global color2
        global color
        global midiin
        global message
        global p
        global mid
        global tempo
        global s
        global next_beat
        global beat_length
        global c
        global beat
        global average

        colorButtonList = [self.color1Button, self.color2Button, self.color3Button, self.color4Button]
        if colorSave % 2 == 1:
            red = int(self.red.text)
            green = int(self.green.text)
            blue = int(self.blue.text)
            colorList[color] = (red, green, blue)
            colorButtonList[color].background_color = (red / 255, green / 255, blue / 255)
            self.red.text = str(colorList[color][0])
            self.green.text = str(colorList[color][1])
            self.blue.text = str(colorList[color][2])
            self.colorSaveButton.text = 'Save Color ' + str(color + 1)
        if colorSave % 2 == 0:
            self.colorSaveButton.background_color = 'gray'
            self.colorSaveButton.text = 'Program Color\n       Button ' + str(color + 1)

        # if sCueRecord % 2 == 1:
        #     self.superCueRecordButton.background_color = 'red'
        # else:
        #     self.superCueRecordButton.background_color = 'gray'


        x = 0
        cueListColors = [self.cue1Button, self.cue2Button, self.cue3Button, self.cue4Button, self.cue5Button, self.cue6Button, self.cue7Button, self.cue8Button]
        for i in allCuesList:
            if cue == x:
                cueListColors[x].background_color = 'red'
            else:
                cueListColors[x].background_color = 'gray'
            x += 1

        x = 0
        # superCueListColors = [self.superCue1Button, self.superCue2Button, self.superCue3Button, self.superCue4Button]
        # for i in superCueListColors:
        #     if sCue == x:
        #         superCueListColors[x].background_color = 'red'
        #     else:
        #         superCueListColors[x].background_color = 'gray'
        #     x += 1

        if save % 2 == 0:
            x = 0
            for i in allCuesList[cue]:
                dmx.set_channel(3 * x + 1, allCuesList[cue][x][0])
                dmx.set_channel(3 * x + 2, allCuesList[cue][x][1])
                dmx.set_channel(3 * x + 3, allCuesList[cue][x][2])
                x += 1

            dmx.submit()
        if save % 2 == 0:
            self.ids.setChannel.background_color = 'gray'

        if save % 2 == 1:
            self.ids.setChannel.background_color = 'red'
            red = self.red.text
            green = self.green.text
            blue = self.blue.text

            if channelLow == '':
                channelLow = 0
            else:
                channelLow = int(channelLow)
            if channelHigh == '':
                channelHigh = 0
            else:
                channelHigh = int(channelHigh)
            if red != '':
                red = int(red)
            if green != '':
                green = int(green)
            if blue != '':
                blue = int(blue)


            if channelLow != '' and red != '' and green != '' and blue != '' and channelHigh != '':
                if channelHigh > len(allCuesList[cue]):
                    channelHigh = len(allCuesList[cue])
                if channelHigh < 0:
                    channelHigh = 0
                if channelLow > len(allCuesList[cue]):
                    channelLow = len(allCuesList[cue])
                if channelLow < 0:
                    channelLow = 0

                x = channelLow - 1
                for i in range((channelHigh - channelLow) + 1):
                    dmx.set_channel(channelsPerFixture * x + 1, red)  # Sets DMX channel 1 to max 255
                    dmx.set_channel(channelsPerFixture * x + 2, green)  # Sets DMX channel 1 to max 255
                    dmx.set_channel(channelsPerFixture * x + 3, blue)  # Sets DMX channel 1 to max 255
                    allCuesList[cue][x].append(red)
                    allCuesList[cue][x].append(green)
                    allCuesList[cue][x].append(blue)
                    allCuesList[cue][x].pop(0)
                    allCuesList[cue][x].pop(0)
                    allCuesList[cue][x].pop(0)

                    # print(channelLow)
                    # print(channelHigh)
                    # print(dmxNumber)

                    x += 1
            dmx.submit()

        res = isinstance(self.red.text, int)
        ges = isinstance(self.green.text, int)
        bes = isinstance(self.blue.text, int)

        #self.ids.slider_label_red.text = str(self.red.text)
        if res is False:
            self.ids.slider_red.value = int(self.red.text)
            if int(self.red.text) > 255:
                self.ids.slider_red.value = 255
            if int(self.red.text) < 0:
                self.ids.slider_red.value = 0
        if ges is False:
            self.ids.slider_green.value = int(self.green.text)
            if int(self.green.text) > 255:
                self.ids.slider_green.value = 255
            if int(self.green.text) < 0:
                self.ids.slider_green.value = 0
        if bes is False:
            self.ids.slider_blue.value = int(self.blue.text)
            if int(self.blue.text) > 255:
                self.ids.slider_blue.value = 255
            if int(self.blue.text) < 0:
                self.ids.slider_blue.value = 0


        timingLoop = Clock.schedule_once(self.timing, .01)

        #
        # if play % 2 == 1:
        #     timingLoop = Clock.schedule_once(self.timing, .125)
        #     self.playButton.background_color = 'red'
        #     if len(superCueList[sCue]) > 0:
        #         cue = superCueList[sCue][c]
        #         dmx.submit()
        #         c += 1
        #         if c == len(superCueList[sCue]):
        #             c = 0


class MyApp(App):
    def build(self):
        return MyLayout()


# run Say Hello App Calss
if __name__ == "__main__":
    MyApp().run()