#-------------------------------------------------------------------------------
# Name:        List06
# Purpose:
#
# Author:      holly long, emilie rabeau
#
# Created:     18-01-2018
# Copyright:   (c) holly 2018
# Licence:     <your licence>
#-------------------------------------------------------------------------------
# Command Line Arugument used: ..\..\..\Data

import os
import sys
arcpy=None

def setArcPy():
    global arcpy
    if arcpy == None:
        import arcpy

if len(sys.argv) != 2:
    print "Usage: List06.py <RootFolder>"
    sys.exit()

else:
    setArcPy()

    arcpy.env.workspace = sys.argv[1]

    if arcpy.Exists(sys.argv[1]):
        for root, dirs, files in os.walk(sys.argv[1]):
            arcpy.env.workspace = root
            workspaces = arcpy.ListWorkspaces('*','All')

            for workspace in workspaces:
                print os.path.abspath(workspace)

    else:
        print "{} does not exists".format(root)

