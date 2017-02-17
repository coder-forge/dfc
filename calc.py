import wx

############################################################################################################################

version = '0.1.17021720'
appTitle= "CoderForge Calculator"


############################################################################################################################
# our own Frame class based on wx.Frame
class MainFrame(wx.Frame):

    color = {
        # Uniform colors
        'BG'    : "#BABABA",
        'Red'   : "#C05555",
        'Blue'  : "#5590DD",
        'Gray'  : "#B0B0B0",
        'Green' : "#55AA55",
    }

    # the constructor takes 4 arguments
    def __init__(self, parent, title, size):
        wx.Frame.__init__(self, parent, title=title, size=size)

        self.NumpadDigits = (wx.WXK_NUMPAD0, wx.WXK_NUMPAD1, wx.WXK_NUMPAD2, wx.WXK_NUMPAD3, wx.WXK_NUMPAD4, wx.WXK_NUMPAD5, wx.WXK_NUMPAD6, wx.WXK_NUMPAD7, wx.WXK_NUMPAD8, wx.WXK_NUMPAD9)
        self.floating = False
        self.btn = {}

        # here we call a method to setup the visual aspect of the user interface
        self.init_gui()

        # here we bind the events with a respective handler methods
        # common practice is to reflect this binding in the names, like
        # "EVT_CLOSE" for a close event, and "OnClose" for its handler
        wx.EVT_CLOSE(self, self.OnClose)
        wx.EVT_CHAR_HOOK(self, self.OnKeyDown)

        # here we finalize the creation of our main frame (instance of MainFrame class),
        # calling the standard methods to position, arrange and show the frame on screen
        self.Centre()
        self.Layout()
        self.ShowWithEffect(wx.SHOW_EFFECT_BLEND, 400)


    #=====================================================================
    # User Interface methods
    #========================

    # here we define the content of the main frame sizer
    def init_gui(self):

        # here we introduce 3 separate fonts, one for each panel
        self.buttonsFont = wx.Font(15, wx.TELETYPE, wx.FONTSTYLE_NORMAL, wx.NORMAL, faceName="Ubuntu Mono")
        self.displayFont = wx.Font(15, wx.TELETYPE, wx.FONTSTYLE_NORMAL, wx.NORMAL, faceName="Liberation Mono")
        self.historyFont = wx.Font(12, wx.TELETYPE, wx.FONTSTYLE_NORMAL, wx.NORMAL, faceName="Liberation Mono")

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
        # possibly we don't need these intermediate variables above?

        # we use simple top-down sizer
        sizer = wx.BoxSizer(wx.VERTICAL)

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
        #self.SetSizeHints(self)
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
        panel = wx.Panel(self)
        panel.SetBackgroundColour('#55BADA')
        panel.SetFont(self.displayFont)

        self.display = wx.TextCtrl(panel, style=wx.TE_RIGHT)
        self.display.SetValue("0")

        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(self.display, 0, wx.EXPAND|wx.BOTTOM, 8)
        panel.SetSizerAndFit(sizer)
        return panel

    def make_buttonsPanel(self):
        panel = self.make_panel((200,200), '#DA55BA')

        # instead of setting certain attributes (like font and event handler) to the individual buttons,
        # we assign them to a parent Panel, from which the buttons will inherit
        panel.SetFont(self.buttonsFont)
        panel.Bind(wx.EVT_BUTTON, self.OnButton)

        # we need such a table-like collection (a tuple of tuples), where we store the button attributes
        # in order to be able to retrieve them in a loop below, sorta line-by-line
        buttons = (
        #   Name_  Label______  Color______________  Pos___  Span__
            ('C',   "C",        self.color['Red'],   (0,0),  (1,1)),
            ('p',   "(",        self.color['Blue'],  (0,1),  (1,1)),
            ('q',   ")",        self.color['Blue'],  (0,2),  (1,1)),
            ('P',   "%",        self.color['Blue'],  (0,3),  (1,1)),
            ('B',   u"\u2190",  self.color['Red'],   (0,4),  (1,1)),
            ('7',   "7",        self.color['Gray'],  (1,0),  (1,1)),
            ('8',   "8",        self.color['Gray'],  (1,1),  (1,1)),
            ('9',   "9",        self.color['Gray'],  (1,2),  (1,1)),
            ('D',   u"\u00F7",  self.color['Blue'],  (1,3),  (1,1)),
            ('S',   u"\u2212",  self.color['Blue'],  (1,4),  (1,1)),
            ('4',   "4",        self.color['Gray'],  (2,0),  (1,1)),
            ('5',   "5",        self.color['Gray'],  (2,1),  (1,1)),
            ('6',   "6",        self.color['Gray'],  (2,2),  (1,1)),
            ('M',   u"\u00D7",  self.color['Blue'],  (2,3),  (1,1)),
            ('A',   "+",        self.color['Blue'],  (2,4),  (2,1)),
            ('1',   "1",        self.color['Gray'],  (3,0),  (1,1)),
            ('2',   "2",        self.color['Gray'],  (3,1),  (1,1)),
            ('3',   "3",        self.color['Gray'],  (3,2),  (1,1)),
            ('R',   u"\u221A",  self.color['Blue'],  (3,3),  (1,1)),
            ('N',   u"\u00B1",  self.color['Blue'],  (4,0),  (1,1)),
            ('0',   "0",        self.color['Gray'],  (4,1),  (1,1)),
            ('F',   ".",        self.color['Gray'],  (4,2),  (1,1)),
            ('E',   "=",        self.color['Green'], (4,3),  (1,2)),
        )

        sizer = wx.GridBagSizer(0,0)

        # here we attempt to replace the individual creation of buttons with a loop.
        # how does it work?
        # in each iteration we read a chunk of attributes from the "buttons" collection defined above,
        # then we create and configure a new button based on these attributes
        # and finlly we add each newly created button to the sizer
        for (name, label, color, pos, spn) in buttons:
            self.btn[name] = wx.Button(panel, label=label, size=(36,36))
            self.btn[name].SetBackgroundColour(color)
            sizer.Add(self.btn[name], pos, span=spn, flag=wx.EXPAND|wx.ALL, border=2)

        # since our loop above appears to work well, we can scratch the individual instrutions below:

        #self.btn_C = wx.Button(panel, label='C', size=(36,36))
        #self.btn_C.SetBackgroundColour('#E08080')

        #self.btn_p = wx.Button(panel, label='(', size=(36,36))
        #self.btn_p.SetBackgroundColour('#55AAFF')

        #self.btn_q = wx.Button(panel, label=')', size=(36,36))
        #self.btn_q.SetBackgroundColour('#55AAFF')

        #self.btn_P = wx.Button(panel, label='%', size=(36,36))
        #self.btn_P.SetBackgroundColour('#55AAFF')
        ##self.btn_B = wx.Button(panel, label=u'\u2190', size=(36,36))
        #self.btn_B = wx.Button(panel, label=u'\N{leftwards white arrow}', size=(36,36))
        #self.btn_B.SetBackgroundColour('#E08080')
        #self.btn['B'].SetFont(self.buttonsFont.MakeLarger())

        #self.btn_7 = wx.Button(panel, label='7', size=(36,36))
        #self.btn_8 = wx.Button(panel, label='8', size=(36,36))
        #self.btn_9 = wx.Button(panel, label='9', size=(36,36))

        #self.btn_D = wx.Button(panel, label=u'\N{division sign}', size=(36,36))
        #self.btn_D.SetBackgroundColour('#55AAFF')
        #self.btn_S = wx.Button(panel, label=u'\N{minus sign}', size=(36,36))
        #self.btn_S.SetBackgroundColour('#55AAFF')

        #self.btn_4 = wx.Button(panel, label='4', size=(36,36))
        #self.btn_5 = wx.Button(panel, label='5', size=(36,36))
        #self.btn_6 = wx.Button(panel, label='6', size=(36,36))

        #self.btn_M = wx.Button(panel, label=u'\N{multiplication sign}', size=(36,36))
        #self.btn_M.SetBackgroundColour('#55AAFF')
        #self.btn_A = wx.Button(panel, label='+', size=(36,36))
        #self.btn_A.SetBackgroundColour('#55AAFF')

        #self.btn_1 = wx.Button(panel, label='1', size=(36,36))
        #self.btn_2 = wx.Button(panel, label='2', size=(36,36))
        #self.btn_3 = wx.Button(panel, label='3', size=(36,36))

        #self.btn_R = wx.Button(panel, label=u'\N{square root}', size=(36,36))
        #self.btn_R.SetBackgroundColour('#55AAFF')
        #self.btn_N = wx.Button(panel, label=u'\N{plus-minus sign}', size=(36,36))
        #self.btn_N.SetBackgroundColour('#55AAFF')

        #self.btn_0 = wx.Button(panel, label='0', size=(36,36))

        #self.btn_F = wx.Button(panel, label='.', size=(36,36))
        #self.btn_E = wx.Button(panel, label='=', size=(36,36))
        #self.btn_E.SetBackgroundColour('#55AA55')

        #sizer.Add(self.btn_C, (0,0), flag=wx.EXPAND|wx.ALL, border=2)
        #sizer.Add(self.btn_p, (0,1), flag=wx.EXPAND|wx.ALL, border=2)
        #sizer.Add(self.btn_q, (0,2), flag=wx.EXPAND|wx.ALL, border=2)
        #sizer.Add(self.btn_P, (0,3), flag=wx.EXPAND|wx.ALL, border=2)
        #sizer.Add(self.btn_B, (0,4), flag=wx.EXPAND|wx.ALL, border=2)
        #sizer.Add(self.btn_7, (1,0), flag=wx.EXPAND|wx.ALL, border=2)
        #sizer.Add(self.btn_8, (1,1), flag=wx.EXPAND|wx.ALL, border=2)
        #sizer.Add(self.btn_9, (1,2), flag=wx.EXPAND|wx.ALL, border=2)
        #sizer.Add(self.btn_D, (1,3), flag=wx.EXPAND|wx.ALL, border=2)
        #sizer.Add(self.btn_S, (1,4), flag=wx.EXPAND|wx.ALL, border=2)
        #sizer.Add(self.btn_4, (2,0), flag=wx.EXPAND|wx.ALL, border=2)
        #sizer.Add(self.btn_5, (2,1), flag=wx.EXPAND|wx.ALL, border=2)
        #sizer.Add(self.btn_6, (2,2), flag=wx.EXPAND|wx.ALL, border=2)
        #sizer.Add(self.btn_M, (2,3), flag=wx.EXPAND|wx.ALL, border=2)
        ## the ADD btn will stretch through 2 rows
        #sizer.Add(self.btn_A, (2,4), span=(2,1), flag=wx.EXPAND|wx.ALL, border=2)
        #sizer.Add(self.btn_1, (3,0), flag=wx.EXPAND|wx.ALL, border=2)
        #sizer.Add(self.btn_2, (3,1), flag=wx.EXPAND|wx.ALL, border=2)
        #sizer.Add(self.btn_3, (3,2), flag=wx.EXPAND|wx.ALL, border=2)
        #sizer.Add(self.btn_R, (3,3), flag=wx.EXPAND|wx.ALL, border=2)
        #sizer.Add(self.btn_N, (4,0), flag=wx.EXPAND|wx.ALL, border=2)
        #sizer.Add(self.btn_0, (4,1), flag=wx.EXPAND|wx.ALL, border=2)
        #sizer.Add(self.btn_F, (4,2), flag=wx.EXPAND|wx.ALL, border=2)
        ## the EQUALS button will stretch through 2 columns
        #sizer.Add(self.btn_E, (4,3), span=(1,2), flag=wx.EXPAND|wx.ALL, border=2)

        panel.SetSizer(sizer)
        return panel


    #=====================================================================
    # Generic methods
    #=================

    def Clear(self):
        if self.floating == True: self.floating = False     # reset decimal-point flag
        self.display.SetValue("0")                          # arbitrarily reset display string

    def DecPt(self, pt):
        if self.floating == False:
            self.floating = True
            self.display.SetValue(self.display.GetValue() + pt)


    #=====================================================================
    # Event handlers
    #================

    def OnKeyDown(self, evt):
        key = evt.GetKeyCode()
        value = self.display.GetValue()

        if key == wx.WXK_ESCAPE or key == ord('Q'):
            self.OnClose(evt)

        # Clear key
        elif key == wx.WXK_DELETE or key == ord('C'):
            print "** KEY: CLEAR"
            self.Clear()

        # Floating point (period) key
        elif key in (wx.WXK_NUMPAD_DECIMAL, ord('.'), ord(',')):
            print "** KEY: DEC-PT"
            self.DecPt(".")

        # Numpad number keys
        elif key in self.NumpadDigits:
            print "** KEY: DIGIT (NUMPAD)", chr(ord("0") + key - wx.WXK_NUMPAD0)
            if value == "0": self.display.SetValue("")                      # remove solitary ZERO from display
            self.display.SetValue(self.display.GetValue() + chr(ord("0") + key - wx.WXK_NUMPAD0))       # append digit to display string

        for i in xrange(0,10):
            if key == ord(str(i)):
                print "** KEY: DIGIT", i
                if value == "0": self.display.SetValue("")                  # remove solitary ZERO from display
                self.display.SetValue(self.display.GetValue() + str(i))     # append digit to display string

        evt.Skip()


    def OnButton(self, evt):
        button = evt.GetEventObject()
        #print "Label:", button.GetLabel()
        value = self.display.GetValue()
        #print "Previous value:", value

        # Cancel button
        if button == self.btn['C']:
            self.display.SetValue("0")

        # Backspace button
        if button == self.btn['B']:
            if self.display.GetValue()[-1:] == ".": self.floating = False
            self.display.SetValue(self.display.GetValue()[0:-1])
            if self.display.GetValue() == "": self.display.SetValue("0")

        # Open parenthesis button
        if button == self.btn['p']:
            pass

        # Close parenthesis button
        if button == self.btn['q']:
            pass

        # Percent button
        if button == self.btn['P']:
            pass

        # Number buttons
        if button in (self.btn['1'], self.btn['2'], self.btn['3'], self.btn['4'], self.btn['5'], self.btn['6'], self.btn['7'], self.btn['8'], self.btn['9'], self.btn['0']):
            if value == "0": self.display.SetValue("")
            self.display.SetValue(self.display.GetValue() + button.GetLabel())

        # Floating point button
        elif button == self.btn['F']:
            print "** BTN: DEC-PT"
            self.DecPt(button.GetLabel())

        # Division button
        if button == self.btn['D']:
            pass

        # Subtraction button
        if button == self.btn['S']:
            pass

        # Multiplication button
        if button == self.btn['M']:
            pass

        # Addition button
        if button == self.btn['A']:
            pass

        # Square root button
        if button == self.btn['R']:
            pass

        # Negate button
        if button == self.btn['N']:
            pass

        # Execute (Equals) button
        if button == self.btn['R']:
            pass

        evt.Skip()



    def OnClose(self, event):
        self.HideWithEffect(wx.SHOW_EFFECT_BLEND, 400)
        self.Destroy()
        event.Skip()


############################################################################################################################

if __name__ == '__main__':

    app = wx.App(redirect=True)
    topWindow = MainFrame(None, appTitle, (300,400))
    app.MainLoop()

