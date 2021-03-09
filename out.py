# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'QtDesktopThread.ui'
#
# Created by: PyQt5 UI code generator 5.15.3
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
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
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
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


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())