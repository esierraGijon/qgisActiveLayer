# -----------------------------------------------------------
# Copyright (C) 2021 Enrique Sierra
# -----------------------------------------------------------
# Licensed under the terms of GNU GPL 2
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
# ---------------------------------------------------------------------

from PyQt5.QtWidgets import QAction, QMessageBox

def classFactory(iface):
    return QgisActiveLayer(iface)

class QgisActiveLayer:
    def __init__(self, iface):
        self.iface = iface
        self.nombre = self.iface.activeLayer().name()

    def initGui(self):
        self.action = QAction('Capactiva', self.iface.mainWindow())
        self.action.triggered.connect(self.run)
        self.iface.addToolBarIcon(self.action)

    def unload(self):
        self.iface.removeToolBarIcon(self.action)
        del self.action

    def run(self):
        self.iface.activeLayer().editingStarted.connect(self.inicioEdicion)
        self.iface.activeLayer().editingStopped.connect(self.finEdicion)

    def inicioEdicion(self):
        QMessageBox.information(None, 'Capa activa', 'Comienza la edición de la capa ' + self.nombre)

    def finEdicion(self):
        QMessageBox.information(None, 'Capa activa', 'Finaliza la edición de la capa ' + self.nombre)
