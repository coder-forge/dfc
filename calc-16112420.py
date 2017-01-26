import wx

version = '0.1.16121521'
appTitle= "CoderForge Calculator"


# our own Frame class based on wx.Frame
class MainFrame(wx.Frame):

    # the constructor takes 4 arguments
    def __init__(self, parent, title, size):
        wx.Frame.__init__(self, parent, title=title, size=size)
        
        # here we call a method to setup the visual aspect of the user interface
        self.init_gui()

        # here we bind the events with a respective handler methods
        # common practice is to reflect this binding in the names, like
        # "EVT_CLOSE" for a close event, and "OnClose" for its handler
        wx.EVT_CLOSE(self, self.OnClose)

        # here we finalize the creation of our main frame (instance of MainFrame class), 
        # calling the standard methods to position, arrange and show the frame on screen
        self.Centre()
        self.Layout()
        self.ShowWithEffect(wx.SHOW_EFFECT_BLEND, 1000)


    # here we define the content of the main frame sizer
    def init_gui(self):
    
        # we use simple top-down sizer
        sizer = wx.BoxSizer(wx.VERTICAL)
        
        # we decided that our calculator will have 3 distinct sections:
        # history section, display section and the buttons section
        # for now they will be represented by 3 panels with different colors,
        # that we're going to redefine into something else in the future
        # history section
        historyPanel = self.make_historyPanel()
        # display section
        displayPanel = self.make_displayPanel()
        # buttons section
        buttonsPanel = self.make_buttonsPanel()

        # here we cram the section placeholders into our sizer
        sizer.Add(historyPanel, 0, wx.EXPAND | wx.ALL, 4)
        sizer.Add(displayPanel, 0, wx.EXPAND | wx.ALL, 4)
        sizer.Add(buttonsPanel, 0, wx.EXPAND | wx.ALL, 4)
        
        # the final step - set the sizer
        # this time instead of simple SetSizer we use SetSizerAndFit,
        # this way we impose restrictions on our frame to accommodate all its children
        # - we force it to recalculate its shape (stretch or shrink) upon creation
        # - we prevent it from ever becoming smaller than required
        # important note:
        # with 'self.' prefix we can reach out of this method's body
        # and affect the "Sizer" property of the "MainFrame" object
        self.SetSizerAndFit(sizer)

    def make_panel(self, size, color):
        panel = wx.Panel(self, wx.ID_ANY, size=size)
        panel.SetBackgroundColour(color)
        return panel

    def make_historyPanel(self):
        panel = self.make_panel((200,80), '#BADA55')
        sizer = wx.BoxSizer(wx.VERTICAL)
        panel.SetSizer(sizer)
        return panel

    def make_displayPanel(self):
        panel = self.make_panel((200,40), '#55BADA')
        sizer = wx.BoxSizer(wx.VERTICAL)
        panel.SetSizer(sizer)
        return panel

    def make_buttonsPanel(self):
        panel = self.make_panel((200,200), '#DA55BA')

        font = wx.Font(15, wx.FONTFAMILY_TELETYPE, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, faceName="Consolas")
        panel.SetFont(font)
        
        buttonC = wx.Button(panel, label='C', size=(36,36))
        buttonC.SetBackgroundColour('#E08080')

        sizer = wx.BoxSizer(wx.VERTICAL)
        buttonp = wx.Button(panel, label='(', size=(36,36))
        buttonp.SetBackgroundColour('#55AAFF')
   
        buttonq = wx.Button(panel, label=')', size=(36,36))
        buttonq.SetBackgroundColour('#55AAFF')
   
        buttonP = wx.Button(panel, label='%', size=(36,36))
        buttonP.SetBackgroundColour('#55AAFF')
        #buttonB = wx.Button(panel, label=u'\u2190', size=(36,36))
        buttonB = wx.Button(panel, label=u'\N{leftwards white arrow}', size=(36,36))
        buttonB.SetBackgroundColour('#E08080')
        buttonB.SetFont(font.MakeLarger())

        button7 = wx.Button(panel, label='7', size=(36,36))
        button8 = wx.Button(panel, label='8', size=(36,36))
        button9 = wx.Button(panel, label='9', size=(36,36))

        buttonD = wx.Button(panel, label=u'\N{division sign}', size=(36,36))
        buttonD.SetBackgroundColour('#55AAFF')
        buttonS = wx.Button(panel, label=u'\N{minus sign}', size=(36,36))
        buttonS.SetBackgroundColour('#55AAFF')

        button4 = wx.Button(panel, label='4', size=(36,36))
        button5 = wx.Button(panel, label='5', size=(36,36))
        button6 = wx.Button(panel, label='6', size=(36,36))

        buttonM = wx.Button(panel, label=u'\N{multiplication sign}', size=(36,36))
        buttonM.SetBackgroundColour('#55AAFF')
        buttonA = wx.Button(panel, label='+', size=(36,36))
        buttonA.SetBackgroundColour('#55AAFF')

        button1 = wx.Button(panel, label='1', size=(36,36))
        button2 = wx.Button(panel, label='2', size=(36,36))
        button3 = wx.Button(panel, label='3', size=(36,36))

        buttonR = wx.Button(panel, label=u'\N{square root}', size=(36,36))
        buttonR.SetBackgroundColour('#55AAFF')
        buttonN = wx.Button(panel, label=u'\N{plus-minus sign}', size=(36,36))
        buttonN.SetBackgroundColour('#55AAFF')

        button0 = wx.Button(panel, label='0', size=(36,36))

        button_ = wx.Button(panel, label='.', size=(36,36))
        buttonE = wx.Button(panel, label='=', size=(36,36))
        buttonE.SetBackgroundColour('#55AA55')

        sizer = wx.GridBagSizer(0,0)
        sizer.Add(buttonC, (0,0), flag=wx.EXPAND|wx.ALL, border=2)
        sizer.Add(buttonp, (0,1), flag=wx.EXPAND|wx.ALL, border=2)
        sizer.Add(buttonq, (0,2), flag=wx.EXPAND|wx.ALL, border=2)
        sizer.Add(buttonP, (0,3), flag=wx.EXPAND|wx.ALL, border=2)
        sizer.Add(buttonB, (0,4), flag=wx.EXPAND|wx.ALL, border=2)
        sizer.Add(button7, (1,0), flag=wx.EXPAND|wx.ALL, border=2)
        sizer.Add(button8, (1,1), flag=wx.EXPAND|wx.ALL, border=2)
        sizer.Add(button9, (1,2), flag=wx.EXPAND|wx.ALL, border=2)
        sizer.Add(buttonD, (1,3), flag=wx.EXPAND|wx.ALL, border=2)
        sizer.Add(buttonS, (1,4), flag=wx.EXPAND|wx.ALL, border=2)
        sizer.Add(button4, (2,0), flag=wx.EXPAND|wx.ALL, border=2)
        sizer.Add(button5, (2,1), flag=wx.EXPAND|wx.ALL, border=2)
        sizer.Add(button6, (2,2), flag=wx.EXPAND|wx.ALL, border=2)
        sizer.Add(buttonM, (2,3), flag=wx.EXPAND|wx.ALL, border=2)
        # the ADD button will stretch through 2 rows
        sizer.Add(buttonA, (2,4), span=(2,1), flag=wx.EXPAND|wx.ALL, border=2)
        sizer.Add(button1, (3,0), flag=wx.EXPAND|wx.ALL, border=2)
        sizer.Add(button2, (3,1), flag=wx.EXPAND|wx.ALL, border=2)
        sizer.Add(button3, (3,2), flag=wx.EXPAND|wx.ALL, border=2)
        sizer.Add(buttonR, (3,3), flag=wx.EXPAND|wx.ALL, border=2)
        sizer.Add(buttonN, (4,0), flag=wx.EXPAND|wx.ALL, border=2)
        sizer.Add(button0, (4,1), flag=wx.EXPAND|wx.ALL, border=2)
        sizer.Add(button_, (4,2), flag= wx.EXPAND | wx.ALL, border=2)
        # the EQUALS button will stretch through 2 columns
        sizer.Add(buttonE, (4,3), span=(1,2), flag=wx.EXPAND|wx.ALL, border=2)
        panel.SetSizer(sizer)
        return panel


    # here we define an event handler method, that during initialisation 
    # we associate with respective event (see line 20)
    def OnClose(self, event):
        self.HideWithEffect(wx.SHOW_EFFECT_BLEND, 1000)
        self.Destroy()
        event.Skip()



if __name__ == '__main__':

    app = wx.App(redirect=False)
    topWindow = MainFrame(None, appTitle, (300,400))
    app.MainLoop()

