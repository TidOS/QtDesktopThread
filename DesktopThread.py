#!/usr/bin/env python3
#DesktopThread.py

""" 
    Create a new desktop thread on /g/
    or post in the current desktop thread
"""

import sys
import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import configparser
import os
import argparse
import time
import requests
import json

# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'QtDesktopThread.ui'
#
# Created by: PyQt5 UI code generator 5.15.3
#

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtWidgets import QFileDialog

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("Desktop Thread")
        MainWindow.resize(763, 825)
        MainWindow.setAutoFillBackground(False)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setEnabled(True)
        self.tabWidget.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.tabWidget.setObjectName("tabWidget")
        self.MainTab = QtWidgets.QWidget()
        self.MainTab.setObjectName("MainTab")
        self.formLayout = QtWidgets.QFormLayout(self.MainTab)
        self.formLayout.setObjectName("formLayout")
        self.NameFieldLabel = QtWidgets.QLabel(self.MainTab)
        self.NameFieldLabel.setMinimumSize(QtCore.QSize(69, 34))
        self.NameFieldLabel.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.NameFieldLabel.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByKeyboard|QtCore.Qt.LinksAccessibleByMouse)
        self.NameFieldLabel.setObjectName("NameFieldLabel")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.NameFieldLabel)
        self.NameField = QtWidgets.QLineEdit(self.MainTab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.NameField.sizePolicy().hasHeightForWidth())
        self.NameField.setSizePolicy(sizePolicy)
        self.NameField.setMinimumSize(QtCore.QSize(0, 30))
        self.NameField.setMaximumSize(QtCore.QSize(32768, 20))
        self.NameField.setBaseSize(QtCore.QSize(30, 30))
        self.NameField.setText("")
        self.NameField.setMaxLength(30)
        self.NameField.setFrame(True)
        self.NameField.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.NameField.setClearButtonEnabled(True)
        self.NameField.setObjectName("NameField")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.NameField)
        self.CommentFieldLabel = QtWidgets.QLabel(self.MainTab)
        self.CommentFieldLabel.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.CommentFieldLabel.setObjectName("CommentFieldLabel")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.CommentFieldLabel)
        self.CommentField = QtWidgets.QTextEdit(self.MainTab)
        self.CommentField.setMaximumSize(QtCore.QSize(32768, 100))
        self.CommentField.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.CommentField.setTabChangesFocus(True)
        self.CommentField.setAcceptRichText(False)
        self.CommentField.setObjectName("CommentField")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.CommentField)
        self.DesktopPreview = QtWidgets.QLabel(self.MainTab)
        self.DesktopPreview.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.DesktopPreview.sizePolicy().hasHeightForWidth())
        self.DesktopPreview.setSizePolicy(sizePolicy)
        self.DesktopPreview.setMinimumSize(QtCore.QSize(640, 360))
        self.DesktopPreview.setMaximumSize(QtCore.QSize(640, 360))
        self.DesktopPreview.setAcceptDrops(True)
        self.DesktopPreview.setStatusTip("")
        self.DesktopPreview.setAutoFillBackground(False)
        self.DesktopPreview.setFrameShape(QtWidgets.QFrame.Box)
        self.DesktopPreview.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.DesktopPreview.setLineWidth(3)
        self.DesktopPreview.setMidLineWidth(2)
        self.DesktopPreview.setText("")
        self.DesktopPreview.setTextFormat(QtCore.Qt.RichText)
        self.DesktopPreview.setPixmap(QtGui.QPixmap("Tidus.jpg"))
        self.DesktopPreview.setScaledContents(True)
        self.DesktopPreview.setWordWrap(True)
        self.DesktopPreview.setObjectName("DesktopPreview")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.DesktopPreview)
        self.ThreadLabel = QtWidgets.QLabel(self.MainTab)
        self.ThreadLabel.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft)
        self.ThreadLabel.setObjectName("ThreadLabel")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.ThreadLabel)
        self.widget = QtWidgets.QWidget(self.MainTab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget.sizePolicy().hasHeightForWidth())
        self.widget.setSizePolicy(sizePolicy)
        self.widget.setMaximumSize(QtCore.QSize(16777215, 52))
        self.widget.setObjectName("widget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.ThreadComboBox = QtWidgets.QComboBox(self.widget)
        self.ThreadComboBox.setMaximumSize(QtCore.QSize(200, 16777215))
        self.ThreadComboBox.setCurrentText("")
        self.ThreadComboBox.setObjectName("ThreadComboBox")
        self.horizontalLayout.addWidget(self.ThreadComboBox, 0, QtCore.Qt.AlignVCenter)
        self.NewThreadCheckBox = QtWidgets.QCheckBox(self.widget)
        self.NewThreadCheckBox.setObjectName("NewThreadCheckBox")
        self.horizontalLayout.addWidget(self.NewThreadCheckBox, 0, QtCore.Qt.AlignVCenter)
        self.BlankThreadSpacerLabel = QtWidgets.QLabel(self.widget)
        self.BlankThreadSpacerLabel.setText("")
        self.BlankThreadSpacerLabel.setObjectName("BlankThreadSpacerLabel")
        self.horizontalLayout.addWidget(self.BlankThreadSpacerLabel)
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.widget)
        self.label = QtWidgets.QLabel(self.MainTab)
        self.label.setObjectName("label")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.label)
        self.widget_3 = QtWidgets.QWidget(self.MainTab)
        self.widget_3.setObjectName("widget_3")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.widget_3)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.lineEdit = QtWidgets.QLineEdit(self.widget_3)
        self.lineEdit.setMaximumSize(QtCore.QSize(16777215, 40))
        self.lineEdit.setObjectName("lineEdit")
        self.horizontalLayout_3.addWidget(self.lineEdit)
        self.toolButton = QtWidgets.QToolButton(self.widget_3)
        self.toolButton.setMaximumSize(QtCore.QSize(16777215, 40))
        self.toolButton.setObjectName("toolButton")
        self.horizontalLayout_3.addWidget(self.toolButton)
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.widget_3)
        self.tabWidget.addTab(self.MainTab, "")
        self.GoldOptionsTab = QtWidgets.QWidget()
        self.GoldOptionsTab.setObjectName("GoldOptionsTab")
        self.formLayout_2 = QtWidgets.QFormLayout(self.GoldOptionsTab)
        self.formLayout_2.setObjectName("formLayout_2")
        self.TokenLabel = QtWidgets.QLabel(self.GoldOptionsTab)
        self.TokenLabel.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.TokenLabel.setObjectName("TokenLabel")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.TokenLabel)
        self.TokenInputField = QtWidgets.QLineEdit(self.GoldOptionsTab)
        self.TokenInputField.setMaximumSize(QtCore.QSize(800, 100))
        self.TokenInputField.setEchoMode(QtWidgets.QLineEdit.PasswordEchoOnEdit)
        self.TokenInputField.setObjectName("TokenInputField")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.TokenInputField)
        self.PinLabel = QtWidgets.QLabel(self.GoldOptionsTab)
        self.PinLabel.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.PinLabel.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.PinLabel.setIndent(-1)
        self.PinLabel.setObjectName("PinLabel")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.PinLabel)
        self.PinInputField = QtWidgets.QLineEdit(self.GoldOptionsTab)
        self.PinInputField.setMaximumSize(QtCore.QSize(800, 100))
        self.PinInputField.setEchoMode(QtWidgets.QLineEdit.PasswordEchoOnEdit)
        self.PinInputField.setObjectName("PinInputField")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.PinInputField)
        self.BlankFillerForGoldCheckbox = QtWidgets.QLabel(self.GoldOptionsTab)
        self.BlankFillerForGoldCheckbox.setText("")
        self.BlankFillerForGoldCheckbox.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.BlankFillerForGoldCheckbox.setObjectName("BlankFillerForGoldCheckbox")
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.BlankFillerForGoldCheckbox)
        self.GoldAccountCheckbox = QtWidgets.QCheckBox(self.GoldOptionsTab)
        self.GoldAccountCheckbox.setObjectName("GoldAccountCheckbox")
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.GoldAccountCheckbox)
        self.tabWidget.addTab(self.GoldOptionsTab, "")
        self.SystemTab = QtWidgets.QWidget()
        self.SystemTab.setEnabled(True)
        self.SystemTab.setMaximumSize(QtCore.QSize(16777215, 600))
        self.SystemTab.setObjectName("SystemTab")
        self.gridlayout = QtWidgets.QGridLayout(self.SystemTab)
        self.gridlayout.setObjectName("gridlayout")
        self.webdriverLabel = QtWidgets.QLabel(self.SystemTab)
        self.webdriverLabel.setMaximumSize(QtCore.QSize(16777215, 40))
        self.webdriverLabel.setObjectName("webdriverLabel")
        self.gridlayout.addWidget(self.webdriverLabel, 0, 0, 1, 1)
        self.WebBrowserFileChoose = QtWidgets.QToolButton(self.SystemTab)
        self.WebBrowserFileChoose.setMaximumSize(QtCore.QSize(16777215, 40))
        self.WebBrowserFileChoose.setObjectName("WebBrowserFileChoose")
        self.gridlayout.addWidget(self.WebBrowserFileChoose, 5, 3, 1, 1)
        self.WebBrowserLabel = QtWidgets.QLabel(self.SystemTab)
        self.WebBrowserLabel.setMaximumSize(QtCore.QSize(16777215, 40))
        self.WebBrowserLabel.setObjectName("WebBrowserLabel")
        self.gridlayout.addWidget(self.WebBrowserLabel, 5, 0, 1, 1)
        self.RunBrowserCheckbox = QtWidgets.QCheckBox(self.SystemTab)
        self.RunBrowserCheckbox.setMaximumSize(QtCore.QSize(16777215, 40))
        self.RunBrowserCheckbox.setObjectName("RunBrowserCheckbox")
        self.gridlayout.addWidget(self.RunBrowserCheckbox, 6, 1, 1, 1)
        self.WebBrowserInput = QtWidgets.QLineEdit(self.SystemTab)
        self.WebBrowserInput.setMaximumSize(QtCore.QSize(16777215, 40))
        self.WebBrowserInput.setObjectName("WebBrowserInput")
        self.gridlayout.addWidget(self.WebBrowserInput, 5, 1, 1, 1)
        self.ScrotCommandInput = QtWidgets.QLineEdit(self.SystemTab)
        self.ScrotCommandInput.setMaximumSize(QtCore.QSize(800, 40))
        self.ScrotCommandInput.setObjectName("ScrotCommandInput")
        self.gridlayout.addWidget(self.ScrotCommandInput, 3, 1, 1, 1)
        self.WebDriverFileChoose = QtWidgets.QToolButton(self.SystemTab)
        self.WebDriverFileChoose.setMaximumSize(QtCore.QSize(16777215, 40))
        self.WebDriverFileChoose.setCheckable(False)
        self.WebDriverFileChoose.setObjectName("WebDriverFileChoose")
        self.gridlayout.addWidget(self.WebDriverFileChoose, 0, 3, 1, 1)
        self.checkBox = QtWidgets.QCheckBox(self.SystemTab)
        self.checkBox.setEnabled(False)
        self.checkBox.setMaximumSize(QtCore.QSize(16777215, 40))
        self.checkBox.setObjectName("checkBox")
        self.gridlayout.addWidget(self.checkBox, 1, 1, 1, 1)
        self.ScrotCommandLabel = QtWidgets.QLabel(self.SystemTab)
        self.ScrotCommandLabel.setMaximumSize(QtCore.QSize(16777215, 40))
        self.ScrotCommandLabel.setObjectName("ScrotCommandLabel")
        self.gridlayout.addWidget(self.ScrotCommandLabel, 3, 0, 1, 1)
        self.WebDriverInput = QtWidgets.QLineEdit(self.SystemTab)
        self.WebDriverInput.setMaximumSize(QtCore.QSize(800, 40))
        self.WebDriverInput.setText("")
        self.WebDriverInput.setObjectName("WebDriverInput")
        self.gridlayout.addWidget(self.WebDriverInput, 0, 1, 1, 1)
        self.HeadlessBlank2 = QtWidgets.QLabel(self.SystemTab)
        self.HeadlessBlank2.setMaximumSize(QtCore.QSize(16777215, 40))
        self.HeadlessBlank2.setText("")
        self.HeadlessBlank2.setObjectName("HeadlessBlank2")
        self.gridlayout.addWidget(self.HeadlessBlank2, 7, 3, 1, 1, QtCore.Qt.AlignTop)
        self.tabWidget.addTab(self.SystemTab, "")
        self.gridLayout.addWidget(self.tabWidget, 1, 0, 1, 1)
        self.widget_2 = QtWidgets.QWidget(self.centralwidget)
        self.widget_2.setEnabled(True)
        self.widget_2.setMaximumSize(QtCore.QSize(16777215, 60))
        self.widget_2.setObjectName("widget_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.widget_2)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.SaveButton = QtWidgets.QPushButton(self.widget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.SaveButton.sizePolicy().hasHeightForWidth())
        self.SaveButton.setSizePolicy(sizePolicy)
        self.SaveButton.setObjectName("SaveButton")
        self.horizontalLayout_2.addWidget(self.SaveButton)
        self.LoadButton = QtWidgets.QPushButton(self.widget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.LoadButton.sizePolicy().hasHeightForWidth())
        self.LoadButton.setSizePolicy(sizePolicy)
        self.LoadButton.setObjectName("LoadButton")
        self.horizontalLayout_2.addWidget(self.LoadButton)
        self.PostButtonSpacerLabel = QtWidgets.QLabel(self.widget_2)
        self.PostButtonSpacerLabel.setText("")
        self.PostButtonSpacerLabel.setObjectName("PostButtonSpacerLabel")
        self.horizontalLayout_2.addWidget(self.PostButtonSpacerLabel)
        self.PostButton = QtWidgets.QPushButton(self.widget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.PostButton.sizePolicy().hasHeightForWidth())
        self.PostButton.setSizePolicy(sizePolicy)
        self.PostButton.setObjectName("PostButton")
        self.horizontalLayout_2.addWidget(self.PostButton)
        self.gridLayout.addWidget(self.widget_2, 4, 0, 1, 1)
        self.DesktopHeader = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.DesktopHeader.sizePolicy().hasHeightForWidth())
        self.DesktopHeader.setSizePolicy(sizePolicy)
        self.DesktopHeader.setMaximumSize(QtCore.QSize(32768, 26))
        self.DesktopHeader.setTextFormat(QtCore.Qt.RichText)
        self.DesktopHeader.setAlignment(QtCore.Qt.AlignCenter)
        self.DesktopHeader.setObjectName("DesktopHeader")
        self.gridLayout.addWidget(self.DesktopHeader, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.actionSave = QtWidgets.QAction(MainWindow)
        self.actionSave.setObjectName("actionSave")
        self.actionLoad = QtWidgets.QAction(MainWindow)
        self.actionLoad.setObjectName("actionLoad")
        self.actionOpen = QtWidgets.QAction(MainWindow)
        self.actionOpen.setObjectName("actionOpen")
        self.NameFieldLabel.setBuddy(self.NameField)
        self.CommentFieldLabel.setBuddy(self.CommentField)
        self.ThreadLabel.setBuddy(self.ThreadComboBox)
        self.label.setBuddy(self.lineEdit)
        self.webdriverLabel.setBuddy(self.WebDriverInput)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "DesktopThread"))
        self.NameFieldLabel.setText(_translate("MainWindow", "Name:"))
        self.NameField.setPlaceholderText(_translate("MainWindow", "Anonymous"))
        self.CommentFieldLabel.setText(_translate("MainWindow", "Comment:"))
        self.CommentField.setPlaceholderText(_translate("MainWindow", "Is this the current desktop thread?"))
        self.DesktopPreview.setToolTip(_translate("MainWindow", "Preview of desktop"))
        self.ThreadLabel.setText(_translate("MainWindow", "Thread: "))
        self.ThreadComboBox.setPlaceholderText(_translate("MainWindow", "Choose Thread to Post in"))
        self.NewThreadCheckBox.setText(_translate("MainWindow", "Force New Thread"))
        self.label.setText(_translate("MainWindow", "File:"))
        self.lineEdit.setPlaceholderText(_translate("MainWindow", "/home/anon/post.png"))
        self.toolButton.setText(_translate("MainWindow", "..."))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.MainTab), _translate("MainWindow", "Main"))
        self.TokenLabel.setText(_translate("MainWindow", "Token:"))
        self.TokenInputField.setPlaceholderText(_translate("MainWindow", "Your 4channel pass token"))
        self.PinLabel.setText(_translate("MainWindow", "PIN: "))
        self.PinInputField.setPlaceholderText(_translate("MainWindow", "Your 4channel pass PIN "))
        self.GoldAccountCheckbox.setToolTip(_translate("MainWindow", "If disabled, you cannot use headless mode!"))
        self.GoldAccountCheckbox.setText(_translate("MainWindow", "Gold Account Enabled"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.GoldOptionsTab), _translate("MainWindow", "Gold"))
        self.webdriverLabel.setText(_translate("MainWindow", "Web driver: "))
        self.WebBrowserFileChoose.setText(_translate("MainWindow", "..."))
        self.WebBrowserLabel.setText(_translate("MainWindow", "Web Browser: "))
        self.RunBrowserCheckbox.setText(_translate("MainWindow", "Run browser after post"))
        self.WebBrowserInput.setPlaceholderText(_translate("MainWindow", "/usr/bin/google-chrome"))
        self.ScrotCommandInput.setPlaceholderText(_translate("MainWindow", "scrot -o /home/anon/post.png"))
        self.WebDriverFileChoose.setText(_translate("MainWindow", "..."))
        self.checkBox.setToolTip(_translate("MainWindow", "Headless mode only works if using gold account, see Gold tab"))
        self.checkBox.setText(_translate("MainWindow", "Run webdriver headless"))
        self.ScrotCommandLabel.setText(_translate("MainWindow", "Scrot command:"))
        self.WebDriverInput.setPlaceholderText(_translate("MainWindow", "ex: /usr/bin/chromedriver"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.SystemTab), _translate("MainWindow", "System"))
        self.tabWidget.setTabToolTip(self.tabWidget.indexOf(self.SystemTab), _translate("MainWindow", "System settings"))
        self.SaveButton.setText(_translate("MainWindow", "Save Config"))
        self.LoadButton.setText(_translate("MainWindow", "Load Config"))
        self.PostButton.setText(_translate("MainWindow", "Post"))
        self.DesktopHeader.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:16pt; font-weight:600;\">DESKTOP THREAD</span></p></body></html>"))
        self.actionSave.setText(_translate("MainWindow", "Save"))
        self.actionLoad.setText(_translate("MainWindow", "Reload"))
        self.actionOpen.setText(_translate("MainWindow", "Open"))

captchatime = 20
config = configparser.ConfigParser()
config.read("desktopthread.cfg")
messagemode = False
    
parser = argparse.ArgumentParser(description='Post desktop on /g/')
#parser.add_argument("-I", "-i", "--init",              help="run through initial setup", action=)
parser.add_argument("-G", "-g", "--gold",              help="sign into 4chan gold", action="store_true")
parser.add_argument("-F", "-f", "--file",    type=str, help="absolute path to file for upload, overrides config file")
parser.add_argument("-N", "-n", "--name",    type=str, help="Name to use when posting")
parser.add_argument("-S", "-s", "--sub",     type=str, help="Subject to use if a new thread is made")
parser.add_argument("-C", "-c", "--comment", type=str, help="Comment to use when posting")
parser.add_argument("-T", "-t", "--new",               help="Post a new thread even if one exists", action="store_true")
parser.add_argument("-X", "-x", "--headless",          help="Enable headless mode for webdriver", action="store_true")
parser.add_argument("-D", "-d", "--debug",             help="Enable debug messages", action="store_true")
args = parser.parse_args()

def initBrowser():
    global browser
    if ui.WebDriverInput.text().lower() == "chromedriver":
        from selenium.webdriver.chrome.options import Options
        chrome_options = Options()
        if not goldUser:
            chrome_options.add_experimental_option( "prefs",{'profile.managed_default_content_settings.javascript': 2})
            browser = webdriver.Chrome('chromedriver',options=chrome_options)
        #gold user    
        else:
            if headless:
                chrome_options.add_argument("--headless")
                browser = webdriver.Chrome('chromedriver',options=chrome_options)
            else:
                browser = webdriver.Chrome('chromedriver')
            goldSignin()

    elif ui.WebDriverInput.text().lower() == "geckodriver":
        from selenium.webdriver.firefox.options import Options
        global profile
        global fireFoxOptions
        profile = webdriver.FirefoxProfile()
        options = Options()
        if not goldUser:
            profile.set_preference("javascript.enabled", False)
            browser = webdriver.Firefox(profile, firefox_options=options)
        #gold user
        else:
            if headless:
                options.headless = True
                browser = webdriver.Firefox(profile, firefox_options=options)
            else:
                browser = webdriver.Firefox(profile)
            goldSignin()
        #browser = webdriver.Firefox()
        
    else:
        print("incorrect webdriver value in desktopthread.cfg, use chromedriver or geckodriver")
        exit(1)

    #at this point we have either signed into a gold account or not
    #but we have a browser available to us.
    global postingthread
    postingthread = ""
    if found:
        postingthread = ui.ThreadComboBox.currentText()
        print("posting thread is " + str(postingthread))
        browser.get("https://boards.4chan.org/g/thread/" +str(postingthread))
        browser.find_element_by_id("togglePostFormLink").click()
    else:
        browser.get("https://boards.4chan.org/g/")
        browser.find_element_by_id("togglePostFormLink").click()
        #temporary - subject is just "desktop thread"
        browser.find_element_by_name("sub").send_keys("desktop thread")

    comment = ui.CommentField.toPlainText()
    name = ui.NameField.text()


    browser.find_element_by_name("com").send_keys(comment)
    browser.find_element_by_name("name").send_keys(name)
    browser.find_element_by_name("upfile").send_keys(ui.lineEdit.text())

    if not goldUser:
        WebDriverWait(browser, captchatime).until(lambda driver: 
        browser.find_element_by_xpath("//*[@id=\"g-recaptcha-response\"]").get_attribute("value").strip() != '')
    
    timeout = 5
    browser.find_element_by_name("post").submit()
    '''try:
        element_present = EC.presence_of_element_located((By.CLASS_NAME, 'board-title'))
        WebDriverWait(browser, timeout).until(element_present)
    except TimeoutException:
        print("Timed out waiting for page to load, post failed?")   
    if runbrowser:
        os.system(webbrowser + browser.getCurrentUrl())
    '''
    os.system(webbrowser + " https://boards.4chan.org/g/thread/" + str(postingthread))


def goldSignin():
    browser.get("https://sys.4channel.org/auth")
    token = browser.find_element_by_id("field-id")
    pin = browser.find_element_by_id("field-pin")
    token.send_keys(config['pass']['token'])
    pin.send_keys(config['pass']['pin'])
    pin.submit()
    #wait at most 5 seconds for the logout button to show up before moving on and
    #just going to /g/
    timeout = 5
    try:
        element_present = EC.presence_of_element_located((By.CLASS_NAME, 'msg-success'))
        WebDriverWait(browser, timeout).until(element_present)
    except TimeoutException:
        print("Timed out waiting for page to load or login failed?")   


def greeting():
    print("hello")

def gen_chan():
    for idx, page in enumerate(r):
        for thread in r[idx]['threads']:
            yield thread

def get_threads(key: str, default='NaN'):
    return threads.get(key,default)


def fillUI():
    #name field
    global name
    name = "Anonymous"
    if args.name:
        name = args.Name
    else:
        name = config['post']['name']
    ui.NameField.setText(name)

    #comment field
    global comment
    comment = "desktop thread!"
    if args.comment:
        comment = args.comment
    else:
        comment = config['post']['comment']
    ui.CommentField.setText(comment)

    #file
    global filename
    filename = config['top']['scrot-file']
    ui.lineEdit.setText(filename)
    global scrotcommand
    scrotcommand = config['top']['scrot-cmd']
    ui.ScrotCommandInput.setText(scrotcommand)
    os.system(scrotcommand)
    scrot = QPixmap(filename)
    ui.DesktopPreview.setPixmap(scrot)

    #load up threads
    for i in threadlist:
        ui.ThreadComboBox.addItem(str(i))
    ui.ThreadComboBox.setCurrentIndex(0)

    #4chan gold account info
    global goldUser
    global token
    global pin
    goldUser = False
    token = config['pass']['token']
    pin = config['pass']['pin']
    if args.gold or "y" in config['pass']['gold'].lower():
        goldUser = True
        ui.TokenInputField.setText(token)
        ui.PinInputField.setText(pin)
        ui.GoldAccountCheckbox.setChecked(True)
        ui.checkBox.setEnabled(True)
    
    #system tab
    #try to autodetect webdrivers in future?
    global webdrivername 
    webdrivername = "none"
    webdrivername = config['system']['webdriver']
    ui.WebDriverInput.setText(webdrivername)

    global headless
    headless = False
    if ui.checkBox.isEnabled():
        if args.headless or "y" in config['system']['headless'].lower():
            ui.checkBox.setChecked(True)
            headless = True

    global scrotter
    scrotter = config['top']['scrot-cmd']
    ui.ScrotCommandInput.setText(scrotter)

    global webbrowser
    webbrowser = config['system']['mybrowserpath']
    ui.WebBrowserInput.setText(webbrowser)
    
    global runbrowser
    runbrowser = False
    if "y" in config['system']['openbrowserafterpost'].lower():
        ui.RunBrowserCheckbox.setChecked(True)
        runbrowser = True



def newThreadClicked():
    global newThread 
    newThread = False
    if ui.NewThreadCheckBox.isChecked():
        ui.ThreadComboBox.setEnabled(False)
        newThread = True
    else:
        ui.ThreadComboBox.setEnabled(True)

def goldClicked():
    print("gold account checkbox clicked, it is now " + str(ui.GoldAccountCheckbox.isChecked()))
    if ui.GoldAccountCheckbox.isChecked():
        ui.checkBox.setEnabled(True)
    else:
        ui.checkBox.setEnabled(False)
        ui.checkBox.setChecked(False)

def fileClicked():
    name = QFileDialog.getOpenFileName(ui.toolButton, 'Open File')
    filename = name[0]
    ui.lineEdit.setText(filename)
    ui.DesktopPreview.setPixmap(QPixmap(filename))

def saveConfig():
    config_file = "desktopthread.cfg"
    open_file = open(config_file, 'w')

    #pass section
    open_file.write("[pass]\r\n")
    open_file.write("token = " + token + "\r\n")
    open_file.write("pin = " + pin + "\r\n")
    open_file.write("gold = ")
    open_file.write("Yes" if ui.GoldAccountCheckbox.isChecked() else "No")
    open_file.write("\r\n\r\n")

    #system section
    open_file.write("[system]\r\n")
    open_file.write("webdriver = " + webdrivername + "\r\n")
    open_file.write("headless = ")
    open_file.write("Yes" if headless else "No")
    open_file.write("\r\n")
    open_file.write("openbrowserafterpost = ")
    open_file.write("Yes" if runbrowser else "No")
    open_file.write("\r\n")
    open_file.write("mybrowserpath = " + webbrowser + "\r\n")
    open_file.write("\r\n")

    #top section
    open_file.write("[top]\r\n")
    open_file.write("scrot-cmd = " + scrotter + "\r\n")
    open_file.write("scrot-file = " + filename + "\r\n\r\n")

    #post section
    open_file.write("[post]\r\n")
    open_file.write("subject = " + "desktop thread" + "\r\n")
    open_file.write("comment = " + comment + "\r\n")
    open_file.write("name = " + name + "\r\n")
    open_file.write("forcenewthread = ")
    open_file.write("Yes" if ui.NewThreadCheckBox.isChecked() else "No")
    open_file.write("\r\n")

    open_file.close()

def loadConfig(configPath="./desktopthread.cfg"):
    configPath = QFileDialog.getOpenFileName(ui.LoadButton, 'Open File')[0]
    config.read(configPath)
    fillUI()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    global ui
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()   
    
    #load up all threads on board using json api
    #currently we look for OP posts containing "desktop thread"
    #the first such thread we take as our thread - in the future
    #we could look at all threads that match and choose the best 
    #one based on current replies (is one about to die or was the
    # one we found started prematurely?)
    global r
    r = requests.get('https://a.4cdn.org/g/catalog.json')
    r = r.json()

    global found
    found = False
    global threadlist
    threadlist = []

    for threads in gen_chan():
        com = get_threads('com')
        sub = get_threads('sub')
        no = get_threads('no')
        #desktop thread search string
        if "desktop thread" in com.lower()or "desktop thread" in sub.lower():
            found = True
            threadlist.append(no)
            #print(threadlist)
    
    

    
    fillUI()
    #if we have no config, dump defaults out
    try:
        f = open("desktopthread.cfg")
    except IOError:
        saveConfig()
    finally:
        f.close()
    
    ui.NewThreadCheckBox.clicked.connect(newThreadClicked)
    ui.GoldAccountCheckbox.clicked.connect(goldClicked)
    ui.toolButton.clicked.connect(fileClicked)
    ui.PostButton.clicked.connect(initBrowser)
    ui.SaveButton.clicked.connect(saveConfig)
    ui.LoadButton.clicked.connect(loadConfig)

    
    
    

    #browser = initBrowser()

 
sys.exit(app.exec_())
