# -*- coding: utf-8 -*-
"""
Created on Sat Oct  2 12:48:18 2021

@author: Afshin Salehi

If you want to have a nice folium webmap, but on a GUI!
"""

import io
import sys

import folium
from PyQt5 import QtWidgets, QtWebEngineWidgets

def start(x, y, zoom, tile):
    '''
    Returns a folium map in a QT GUI.

            Parameters:
                    x (float): geographical longitude
                    y (float): geographical latitude
                    zoom (int): The starting zoom level
                    tile(str): Type of map visualization (e.g stamen toner, stamen watercolor, and ... 
                                                          check: 
                                                              https://python-visualization.github.io/folium/modules.html#folium.folium.Map)

            Returns:
                    binary_sum (str): Binary string of the sum of a and b
'''
    app = QtWidgets.QApplication(sys.argv)
    m = folium.Map(location=[x, y], tiles=tile, zoom_start=zoom)
    
    data = io.BytesIO()
    m.save(data, close_file=False)
    
    w = QtWebEngineWidgets.QWebEngineView()
    w.setHtml(data.getvalue().decode())
    w.resize(640, 480)
    w.show()
    
    sys.exit(app.exec_())

start(45.5236, -122.6750, 13, "Stamen Toner")