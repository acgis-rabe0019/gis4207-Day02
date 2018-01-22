#-------------------------------------------------------------------------------
# Name:        List02.py
# Purpose:
#
# Author:      holly long, emilie rabeau
#
# Created:     18-01-2018
# Copyright:   (c) holly 2018
# Licence:     <your licence>
#-------------------------------------------------------------------------------
#Command Line Argument Used: ..\..\..\Data\SanFrancisco

import sys
arcpy = None

def setArcPy():
    global arcpy
    if arcpy == None:
        import arcpy


if len(sys.argv) != 2:
    print "Usage:  List02.py <FeatureClassName>"
    sys.exit()

else:
    setArcPy()

    arcpy.env.workspace=sys.argv[1]

    if arcpy.Exists(sys.argv[1]):
        fclist = arcpy.ListFeatureClasses()
        for f in fclist:
            print f

    else:
        print "{} does not exists".format(fc)

