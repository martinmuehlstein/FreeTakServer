#######################################################
# 
# Precisionlocation.py
# Python implementation of the Class Precisionlocation
# Generated by Enterprise Architect
# Created on:      11-Feb-2020 11:08:10 AM
# Original author: Corvo
# 
#######################################################


class Precisionlocation:
    """some type of location?
    """
    
# TDB can be DTED0 or ???
 

    # default constructor       
    def __init__(self, xml):
        self.altsrc = None
        self.geopointsrc = None
        self.setaltsrc(xml.get('altsrc'))
        self.setgeopointsrc(xml.get('geopointsrc'))

    # geopointsrc getter 
    def getgeopointsrc(self): 
      return self.geopointsrc 
 
     # geopointsrc setter 
    def setgeopointsrc(self, geopointsrc=0):  
        self.geopointsrc=geopointsrc 
    
          # altsrc getter 
    def getaltsrc(self): 
        return self.altsrc 
 
     # altsrc setter 
    def setaltsrc(self, altsrc=0):  
        self.altsrc=altsrc 
 