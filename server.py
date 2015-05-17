import wx 
import wx.html2

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
 
        self.SetIcon(self.icon, "Restore")
        self.Bind(wx.EVT_TASKBAR_LEFT_DOWN, self.OnTaskBarLeftClick)
 
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

if __name__ == '__main__': 
  app = wx.App() 
  dialog = MyBrowser(None, -1,"CMB intercom",pos=(100,100),style=wx.NO_BORDER & wx.STAY_ON_TOP) 
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