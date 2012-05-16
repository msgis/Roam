# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_drawingpad.ui'
#
# Created: Wed May 16 15:52:22 2012
#      by: PyQt4 UI code generator 4.8.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_DrawingWindow(object):
    def setupUi(self, DrawingWindow):
        DrawingWindow.setObjectName(_fromUtf8("DrawingWindow"))
        DrawingWindow.resize(493, 476)
        DrawingWindow.setModal(False)
        self.verticalLayout = QtGui.QVBoxLayout(DrawingWindow)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setMargin(0)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setSizeConstraint(QtGui.QLayout.SetDefaultConstraint)
        self.horizontalLayout_2.setMargin(3)
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.toolClear = QtGui.QToolButton(DrawingWindow)
        self.toolClear.setIconSize(QtCore.QSize(32, 32))
        self.toolClear.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.toolClear.setAutoRaise(True)
        self.toolClear.setObjectName(_fromUtf8("toolClear"))
        self.horizontalLayout_2.addWidget(self.toolClear)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.toolMapSnapshot = QtGui.QToolButton(DrawingWindow)
        self.toolMapSnapshot.setIconSize(QtCore.QSize(32, 32))
        self.toolMapSnapshot.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.toolMapSnapshot.setAutoRaise(True)
        self.toolMapSnapshot.setObjectName(_fromUtf8("toolMapSnapshot"))
        self.horizontalLayout_2.addWidget(self.toolMapSnapshot)
        self.toolRedPen = QtGui.QToolButton(DrawingWindow)
        self.toolRedPen.setIconSize(QtCore.QSize(32, 32))
        self.toolRedPen.setCheckable(True)
        self.toolRedPen.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.toolRedPen.setAutoRaise(True)
        self.toolRedPen.setObjectName(_fromUtf8("toolRedPen"))
        self.buttonGroup = QtGui.QButtonGroup(DrawingWindow)
        self.buttonGroup.setObjectName(_fromUtf8("buttonGroup"))
        self.buttonGroup.addButton(self.toolRedPen)
        self.horizontalLayout_2.addWidget(self.toolRedPen)
        self.toolBluePen = QtGui.QToolButton(DrawingWindow)
        self.toolBluePen.setIconSize(QtCore.QSize(32, 32))
        self.toolBluePen.setCheckable(True)
        self.toolBluePen.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.toolBluePen.setAutoRaise(True)
        self.toolBluePen.setObjectName(_fromUtf8("toolBluePen"))
        self.buttonGroup.addButton(self.toolBluePen)
        self.horizontalLayout_2.addWidget(self.toolBluePen)
        self.toolBlackPen = QtGui.QToolButton(DrawingWindow)
        self.toolBlackPen.setIconSize(QtCore.QSize(32, 32))
        self.toolBlackPen.setCheckable(True)
        self.toolBlackPen.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.toolBlackPen.setAutoRaise(True)
        self.toolBlackPen.setObjectName(_fromUtf8("toolBlackPen"))
        self.buttonGroup.addButton(self.toolBlackPen)
        self.horizontalLayout_2.addWidget(self.toolBlackPen)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.toolSave = QtGui.QToolButton(DrawingWindow)
        self.toolSave.setIconSize(QtCore.QSize(32, 32))
        self.toolSave.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.toolSave.setAutoRaise(True)
        self.toolSave.setObjectName(_fromUtf8("toolSave"))
        self.horizontalLayout_2.addWidget(self.toolSave)
        self.toolCancel = QtGui.QToolButton(DrawingWindow)
        self.toolCancel.setIconSize(QtCore.QSize(32, 32))
        self.toolCancel.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.toolCancel.setAutoRaise(True)
        self.toolCancel.setObjectName(_fromUtf8("toolCancel"))
        self.horizontalLayout_2.addWidget(self.toolCancel)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.frame = QtGui.QFrame(DrawingWindow)
        self.frame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtGui.QFrame.Raised)
        self.frame.setObjectName(_fromUtf8("frame"))
        self.gridLayout_2 = QtGui.QGridLayout(self.frame)
        self.gridLayout_2.setMargin(0)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.verticalLayout.addWidget(self.frame)
        self.actionClearDrawing = QtGui.QAction(DrawingWindow)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/clearimage")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionClearDrawing.setIcon(icon)
        self.actionClearDrawing.setObjectName(_fromUtf8("actionClearDrawing"))
        self.actionRedPen = QtGui.QAction(DrawingWindow)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/redpen")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionRedPen.setIcon(icon1)
        self.actionRedPen.setObjectName(_fromUtf8("actionRedPen"))
        self.actionBluePen = QtGui.QAction(DrawingWindow)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/bluepen")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionBluePen.setIcon(icon2)
        self.actionBluePen.setObjectName(_fromUtf8("actionBluePen"))
        self.actionBlackPen = QtGui.QAction(DrawingWindow)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/blackpen")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionBlackPen.setIcon(icon3)
        self.actionBlackPen.setObjectName(_fromUtf8("actionBlackPen"))
        self.actionSave = QtGui.QAction(DrawingWindow)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/tick")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionSave.setIcon(icon4)
        self.actionSave.setObjectName(_fromUtf8("actionSave"))
        self.actionCancel = QtGui.QAction(DrawingWindow)
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/cancel")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionCancel.setIcon(icon5)
        self.actionCancel.setObjectName(_fromUtf8("actionCancel"))
        self.actionMapSnapshot = QtGui.QAction(DrawingWindow)
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/map")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionMapSnapshot.setIcon(icon6)
        self.actionMapSnapshot.setObjectName(_fromUtf8("actionMapSnapshot"))

        self.retranslateUi(DrawingWindow)
        QtCore.QObject.connect(self.toolSave, QtCore.SIGNAL(_fromUtf8("pressed()")), DrawingWindow.accept)
        QtCore.QObject.connect(self.toolCancel, QtCore.SIGNAL(_fromUtf8("pressed()")), DrawingWindow.reject)
        QtCore.QMetaObject.connectSlotsByName(DrawingWindow)

    def retranslateUi(self, DrawingWindow):
        DrawingWindow.setWindowTitle(QtGui.QApplication.translate("DrawingWindow", "Dialog", None, QtGui.QApplication.UnicodeUTF8))
        self.toolClear.setText(QtGui.QApplication.translate("DrawingWindow", "Clear Drawing", None, QtGui.QApplication.UnicodeUTF8))
        self.toolMapSnapshot.setText(QtGui.QApplication.translate("DrawingWindow", "...", None, QtGui.QApplication.UnicodeUTF8))
        self.toolRedPen.setText(QtGui.QApplication.translate("DrawingWindow", "Red", None, QtGui.QApplication.UnicodeUTF8))
        self.toolBluePen.setText(QtGui.QApplication.translate("DrawingWindow", "Blue", None, QtGui.QApplication.UnicodeUTF8))
        self.toolBlackPen.setText(QtGui.QApplication.translate("DrawingWindow", "Black", None, QtGui.QApplication.UnicodeUTF8))
        self.toolSave.setText(QtGui.QApplication.translate("DrawingWindow", "Save", None, QtGui.QApplication.UnicodeUTF8))
        self.toolCancel.setText(QtGui.QApplication.translate("DrawingWindow", "Cancel", None, QtGui.QApplication.UnicodeUTF8))
        self.actionClearDrawing.setText(QtGui.QApplication.translate("DrawingWindow", "Clear Drawing", None, QtGui.QApplication.UnicodeUTF8))
        self.actionClearDrawing.setToolTip(QtGui.QApplication.translate("DrawingWindow", "Clear the current drawing", None, QtGui.QApplication.UnicodeUTF8))
        self.actionRedPen.setText(QtGui.QApplication.translate("DrawingWindow", "Red Pen", None, QtGui.QApplication.UnicodeUTF8))
        self.actionRedPen.setToolTip(QtGui.QApplication.translate("DrawingWindow", "Change pen colour to red", None, QtGui.QApplication.UnicodeUTF8))
        self.actionBluePen.setText(QtGui.QApplication.translate("DrawingWindow", "Blue Pen", None, QtGui.QApplication.UnicodeUTF8))
        self.actionBluePen.setToolTip(QtGui.QApplication.translate("DrawingWindow", "Change pen colour to blue", None, QtGui.QApplication.UnicodeUTF8))
        self.actionBlackPen.setText(QtGui.QApplication.translate("DrawingWindow", "Black Pen", None, QtGui.QApplication.UnicodeUTF8))
        self.actionBlackPen.setToolTip(QtGui.QApplication.translate("DrawingWindow", "Change pen colour to black", None, QtGui.QApplication.UnicodeUTF8))
        self.actionSave.setText(QtGui.QApplication.translate("DrawingWindow", "Save", None, QtGui.QApplication.UnicodeUTF8))
        self.actionSave.setToolTip(QtGui.QApplication.translate("DrawingWindow", "Save the current image", None, QtGui.QApplication.UnicodeUTF8))
        self.actionCancel.setText(QtGui.QApplication.translate("DrawingWindow", "Cancel", None, QtGui.QApplication.UnicodeUTF8))
        self.actionCancel.setToolTip(QtGui.QApplication.translate("DrawingWindow", "Cancel the current image", None, QtGui.QApplication.UnicodeUTF8))
        self.actionMapSnapshot.setText(QtGui.QApplication.translate("DrawingWindow", "Take Map Snapshot", None, QtGui.QApplication.UnicodeUTF8))

import resources_rc
