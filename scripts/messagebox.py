#!/usr/bin/pyton

#messagebox.py
# from the book
import wx

class MessageDialog(wx.Frame):
    def __init__(self,parent,id,title):
        wx.Frame.__init__(self,parent,id,title)
        wx.FutureCall(1000,self.ShowMessage)
        self.Centre()
        self.Show(True)
    def ShowMessage(self):
        wx.MessageBox('Download completed','Info')

app = wx.App()
MessageDialog(None,-1,'MessageDialog')
app.MainLoop()
