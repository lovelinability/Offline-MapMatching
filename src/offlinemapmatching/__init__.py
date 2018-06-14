# -*- coding: utf-8 -*-
"""
/***************************************************************************
 OfflineMapMatching
                                 A QGIS plugin
 a plugin to for map matching a trajetory using algirthms of viterbi and dijkstra
 Generated by Plugin Builder: http://g-sherman.github.io/Qgis-Plugin-Builder/
                             -------------------
        begin                : 2018-06-14
        copyright            : (C) 2018 by Christoph Junh
        email                : jagodki.cj@gmail.com
        git sha              : $Format:%H$
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
 This script initializes the plugin, making it known to QGIS.
"""


# noinspection PyPep8Naming
def classFactory(iface):  # pylint: disable=invalid-name
    """Load OfflineMapMatching class from file OfflineMapMatching.

    :param iface: A QGIS interface instance.
    :type iface: QgsInterface
    """
    #
    from .offline_map_matching import OfflineMapMatching
    return OfflineMapMatching(iface)
