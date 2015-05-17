import wx 
import wx.html2

ID_ICON_TIMER = wx.NewId()

class CustomTaskBarIcon(wx.TaskBarIcon):
    """ http://www.blog.pythonlibrary.org/2013/07/12/wxpython-how-to-minimize-to-system-tray/"""

    #----------------------------------------------------------------------
    def __init__(self, frame):
        """Constructor"""
        wx.TaskBarIcon.__init__(self)
        self.frame = frame
 
        img = wx.Image("icon.png", wx.BITMAP_TYPE_ANY)
        bmp = wx.BitmapFromImage(img)
        self.icon = wx.EmptyIcon()
        self.icon.CopyFromBitmap(bmp)

        img = wx.Image("iconred.png", wx.BITMAP_TYPE_ANY)
        bmp = wx.BitmapFromImage(img)
        self.icon2 = wx.EmptyIcon()
        self.icon2.CopyFromBitmap(bmp)
		
        self.SetIcon(self.icon, "Restore")
        self.Bind(wx.EVT_TASKBAR_LEFT_DOWN, self.OnTaskBarLeftClick)
        self.icontimer = wx.Timer(self, ID_ICON_TIMER)
        wx.EVT_TIMER(self, ID_ICON_TIMER, self.BlinkIcon)
        self.icontimer.Start(200)
		
        self.blink_high = True
		
    def BlinkIcon(self, evt):
		if self.blink_high:
			self.SetIcon(self.icon, "Restore")
		else:
			self.SetIcon(self.icon2, "Restore")
		self.blink_high = not self.blink_high
    #----------------------------------------------------------------------
    def OnTaskBarActivate(self, evt):
        """"""
        pass
 
    #----------------------------------------------------------------------
    def OnTaskBarClose(self, evt):
        """
        Destroy the taskbar icon and frame from the taskbar icon itself
        """
        self.frame.Close()
 
    #----------------------------------------------------------------------
    def OnTaskBarLeftClick(self, evt):
        """
        Create the right-click menu
        """
        self.frame.Show()
        self.frame.Restore()

class MyBrowser(wx.Dialog): 
	def __init__(self, *args, **kwds): 
		wx.Dialog.__init__(self, *args, **kwds) 
		sizer = wx.BoxSizer(wx.VERTICAL) 
		self.browser = wx.html2.WebView.New(self) 
		sizer.Add(self.browser, 1, wx.EXPAND, 10) 
		self.SetSizer(sizer)
		size = (400,300)
		self.SetSize(size)
		w = wx.SystemSettings.GetMetric(wx.SYS_SCREEN_X)
		h = wx.SystemSettings.GetMetric(wx.SYS_SCREEN_Y)
		margin_bottom = 100
		pos=(w-size[0], h-size[0]-margin_bottom)
		self.SetPosition(pos)

		self.tbIcon = CustomTaskBarIcon(self)
		self.Bind(wx.EVT_ICONIZE, self.onMinimize)
		self.Bind(wx.EVT_CLOSE, self.onClose)

		self.Show()
 
    #----------------------------------------------------------------------
	def onClose(self, evt):
		"""
		Destroy the taskbar icon and the frame
		"""
		self.tbIcon.RemoveIcon()
		self.tbIcon.Destroy()
		self.Destroy()

	#----------------------------------------------------------------------
	def onMinimize(self, event):
		"""
		When minimizing, hide the frame so it "minimizes to tray"
		"""
		self.Hide()

if __name__ == '__main__': 
  app = wx.App() 
  dialog = MyBrowser(None, -1,"CMB intercom",pos=(100,100),style=wx.NO_BORDER) 
  dialog.browser.LoadURL("http://www.google.com") 
  dialog.Show() 
  app.MainLoop() 

  
"""
from Tkinter import *
root = Tk()
root.attributes('-alpha', 0.3)
root.mainloop()
"""
"""import cherrypy

class HelloWorld(object):
    @cherrypy.expose
    def index(self):
        return "Hello world!"

if __name__ == '__main__':
   cherrypy.quickstart(HelloWorld())"""