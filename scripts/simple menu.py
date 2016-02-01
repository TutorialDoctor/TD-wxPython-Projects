
import wx


class Example(wx.Frame):
    
    def __init__(self,*args,**kwargs):
        super(Example, self).__init__(*args,**kwargs)

        self.InitUI()

    def InitUI(self):
        
        # Simple menubar
        menubar = wx.MenuBar()
        
        #Create menu bar object 
        fileMenu = wx.Menu()

        #Create menu object.
        #We Append Menu item to menu object.
        #The first parameter is the id of the menu item.
        #The standard id will automatically add an icon and a shortcut. Ctrl + Q in our case.
        #The second parameter is the name of the menu item.
        #The last parameter defines the short help string that is displayed on the statusbar, when the menu item is selected.
        #Here we did not create a wx.MenuItem explicitly.
        #It was created by the Append() method behind the scenes.
        #The method returns the created menu item.
        #This reference will be used later to bind an event.
        fileItem = fileMenu.Append(wx.ID_EXIT, 'Quit', 'Quit Application')

        #We bind the wx.EVT_MENU of the menu item to the custom OnQuit() method.
        #This method will close the application.
        self.Bind(wx.EVT_MENU, self.OnQuit, fileItem)

        #After that, we append a menu into the menubar.
        #The & character creates an accelerator key.
        #The character that follows the & is underlined.
        #This way the menu is accessible via the Alt + F shortcut.
        #In the end, we call the SetMenuBar() method.
        #This method belongs to the wx.Frame widget. It sets up the menubar.
        menubar.Append(fileMenu, '&File')
        self.SetMenuBar(menubar)
        
        # Set size
        self.SetSize ((300,200))
        self.SetTitle('Simple menu')
        self.Centre()
        self.Show(True)

        #Close        
    def OnQuit(self, e):
        self.Close()
        
# Main Loop OUTSIDE OF CLASS!
def main():
        ex = wx.App()
        Example(None)
        ex.MainLoop()

#Conditional OUTSIDE OF CLASS
if __name__=='__main__':
    main()
#------------------------------


        
        
