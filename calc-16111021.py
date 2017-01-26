import wx

version = '0.1.16111021'
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
        historyPanel = wx.Panel(self, size=(200,80))
        historyPanel.SetBackgroundColour('#BADA55')
        # display section
        displayPanel = wx.Panel(self, size=(200,40))
        displayPanel.SetBackgroundColour('#55BADA')
        # buttons section
        buttonsPanel = wx.Panel(self, size=(200,200))
        buttonsPanel.SetBackgroundColour('#DA55BA')

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

