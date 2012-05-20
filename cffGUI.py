#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
import commands
import sys
import wx

class Tc:
	def __int__(self, textctrl1, textctrl2, textctrl3):
		self.tc1 = textctrl1
		self.tc2 = textctrl2
		self.tc3 = textctrl3

class MyFrame(wx.Frame):
	def __init__(self, parent, id, title):
		wx.Frame.__init__(self, parent, id, title, size=(390, 230))
		panel = wx.Panel(self, -1)
		
		#menu
		menubar = wx.MenuBar()
		file = wx.Menu()
		quit = wx.MenuItem(file, 100, '&Quite\tCtrl+Q')
		file.AppendItem(quit)		
		self.Bind(wx.EVT_MENU, self.OnQuit, id=100)		
		menubar.Append(file, '&File')
		self.SetMenuBar(menubar)
		
		
		#panel
		vbox = wx.BoxSizer(wx.VERTICAL)
		
		hbox1 = wx.BoxSizer(wx.HORIZONTAL)
		st1 = wx.StaticText(panel, -1, 'Search Dir')
		hbox1.Add(st1, 0, wx.RIGHT, 21)
		Tc.tc1 = wx.TextCtrl(panel, -1, commands.getoutput("pwd"))
		hbox1.Add(Tc.tc1, 1)
		vbox.Add(hbox1, 0, wx.EXPAND | wx.LEFT | wx.RIGHT | wx.TOP, 10)
		
		vbox.Add((-1, 5))
		
		hbox2 = wx.BoxSizer(wx.HORIZONTAL)
		st2 = wx.StaticText(panel, -1, 'Search word')
		hbox2.Add(st2, 0, wx.RIGHT, 8)
		Tc.tc2 = wx.TextCtrl(panel, -1)
		hbox2.Add(Tc.tc2, 1)
		vbox.Add(hbox2, 0, wx.EXPAND | wx.LEFT | wx.RIGHT | wx.TOP, 10)
				
		vbox.Add((-1, 5))
		
		hbox3 = wx.BoxSizer(wx.HORIZONTAL)
		st3 = wx.StaticText(panel, -1, 'Dest Dir')
		hbox3.Add(st3, 0, wx.RIGHT, 34)
		Tc.tc3 = wx.TextCtrl(panel, -1)
		hbox3.Add(Tc.tc3, 1)
		vbox.Add(hbox3, 0, wx.EXPAND | wx.LEFT | wx.RIGHT | wx.TOP, 10)
		
		vbox.Add((-1, 5))
		
		hbox4 = wx.BoxSizer(wx.HORIZONTAL)
		st4 = wx.StaticText(panel, -1, 'Current Directory')
		hbox4.Add(st4, 0, wx.RIGHT, 5)
		st5 = wx.StaticText(panel, -1, commands.getoutput("pwd"))
		hbox4.Add(st5, 0, wx.RIGHT, 5)
		vbox.Add(hbox4, 0, wx.EXPAND | wx.LEFT | wx.RIGHT | wx.TOP, 10)
				
		vbox.Add((-1, 25))

		hbox5 = wx.BoxSizer(wx.HORIZONTAL)
		btn = wx.Button(panel,-1 ,'Start', (70, 30))
		hbox5.Add(btn)
		vbox.Add(hbox5, 0, wx.ALIGN_RIGHT | wx.RIGHT, 10)
		
		self.Bind(wx.EVT_BUTTON, self.OnSubmit, btn)
				
		#
		panel.SetSizer(vbox)
		self.Centre()
		self.Show(True)
		
	#defines
	def OnQuit(self, event):
		self.Close()
	
	def OnSubmit(self, event):
		printing =  "find " + Tc.tc1.GetValue() + " -name" + " \"" + Tc.tc2.GetValue() + "\"" + " -exec" + " cp" + " {} " + Tc.tc3.GetValue() + " \\;"
		dlg = wx.MessageDialog(self, printing, "Executing commands, OK?", wx.YES_NO)
		result = dlg.ShowModal()
		if result == wx.ID_YES:
			os.system("find " + Tc.tc1.GetValue() + " -name" + " \"" + Tc.tc2.GetValue() + "\"" + " -exec" + " cp" + " {} " + Tc.tc3.GetValue() + " \\;")
		elif result == wx.ID_NO:
			wx.MessageBox("Push OK", "Try again", wx.OK )
		dlg.Destroy()

#
app  = wx.App()
MyFrame(None, -1, 'uites.py')
app.MainLoop()