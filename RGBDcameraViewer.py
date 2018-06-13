#!/usr/bin/env python
# -*- coding: utf-8 -*-
# -*- Python -*-

"""
 @file RGBDcameraViewer.py
 @brief RGBDcameraViewer
 @date $Date$


"""
import sys
import time
sys.path.append(".")

# capture
import numpy as np
from numpy import array
import cv2

# Import RTM module
import RTC
import OpenRTM_aist

import RGBDCamera

# Import Service implementation class
# <rtc-template block="service_impl">

# </rtc-template>

# Import Service stub modules
# <rtc-template block="consumer_import">
# </rtc-template>


# This module's spesification
# <rtc-template block="module_spec">
rgbdcameraviewer_spec = ["implementation_id", "RGBDcameraViewer", 
         "type_name",         "RGBDcameraViewer", 
         "description",       "RGBDcameraViewer", 
         "version",           "1.0.0", 
         "vendor",            "kanamura", 
         "category",          "ObjectRecognition", 
         "activity_type",     "STATIC", 
         "max_instance",      "1", 
         "language",          "Python", 
         "lang_type",         "SCRIPT",
         "conf.default.frame_width", "640",
         "conf.default.frame_height", "480",
         
         "conf.__widget__.frame_width", "text",
         "conf.__type__.frame_width", "int",
         
         "conf.__widget__.frame_height", "text",
         "conf.__type__.frame_height", "int",
         ""]
# </rtc-template>

##
# @class RGBDcameraViewer
# @brief RGBDcameraViewer
# 
# 
class RGBDcameraViewer(OpenRTM_aist.DataFlowComponentBase):
    
    ##
    # @brief constructor
    # @param manager Maneger Object
    # 
    def __init__(self, manager):
        OpenRTM_aist.DataFlowComponentBase.__init__(self, manager)

        rgbdCameraImage_arg = [None] * ((len(RGBDCamera._d_TimedRGBDCameraImage) - 4) / 2)
        self._d_rgbdCameraImage = RGBDCamera.TimedRGBDCameraImage(*rgbdCameraImage_arg)
        """
        """
        self._rgbdCameraImageIn = OpenRTM_aist.InPort("rgbdCameraImage", self._d_rgbdCameraImage)


        


        # initialize of configuration-data.
        # <rtc-template block="init_conf_param">

        """
        
         - Name:  frame_width
         - DefaultValue: 640
        """
        self._frame_width = [640]

        #self._model = None

        """
        
         - Name:  frame_height
         - DefaultValue: 480
        """
        self._frame_height = [480]

        self._model = None
        
        # </rtc-template>


         
    ##
    #
    # The initialize action (on CREATED->ALIVE transition)
    # formaer rtc_init_entry() 
    # 
    # @return RTC::ReturnCode_t
    # 
    #
    def onInitialize(self):
        # Bind variables and configuration variable
        
        # Set InPort buffers
        self.addInPort("rgbdCameraImage",self._rgbdCameraImageIn)
        self.bindParameter("frame_width", self._frame_width, "640")
        self.bindParameter("frame_height", self._frame_height, "480")
        
        # Set OutPort buffers
        
        # Set service provider to Ports
        
        # Set service consumers to Ports
        
        # Set CORBA Service Ports
        return RTC.RTC_OK
    
    #   ##
    #   # 
    #   # The finalize action (on ALIVE->END transition)
    #   # formaer rtc_exiting_entry()
    #   # 
    #   # @return RTC::ReturnCode_t
    #
    #   # 
    #def onFinalize(self):
    #
    #   return RTC.RTC_OK
    
    #   ##
    #   #
    #   # The startup action when ExecutionContext startup
    #   # former rtc_starting_entry()
    #   # 
    #   # @param ec_id target ExecutionContext Id
    #   #
    #   # @return RTC::ReturnCode_t
    #   #
    #   #
    #def onStartup(self, ec_id):
    #
    #   return RTC.RTC_OK
    
    #   ##
    #   #
    #   # The shutdown action when ExecutionContext stop
    #   # former rtc_stopping_entry()
    #   #
    #   # @param ec_id target ExecutionContext Id
    #   #
    #   # @return RTC::ReturnCode_t
    #   #
    #   #
    #def onShutdown(self, ec_id):
    #
    #   return RTC.RTC_OK
    
        ##
        #
        # The activated action (Active state entry action)
        # former rtc_active_entry()
        #
        # @param ec_id target ExecutionContext Id
        # 
        # @return RTC::ReturnCode_t
        #
        #
    def onActivated(self, ec_id):
        print('Start image view')

        cv2.namedWindow("img", cv2.WINDOW_AUTOSIZE)

        m_img = np.zeros((640, 480, 3), np.uint8)
        
        return RTC.RTC_OK
    
        ##
        #
        # The deactivated action (Active state exit action)
        # former rtc_active_exit()
        #
        # @param ec_id target ExecutionContext Id
        #
        # @return RTC::ReturnCode_t
        #
        #
    def onDeactivated(self, ec_id):

        
        cv2.destroyAllWindows()
        print("Stop image view.")
        
        return RTC.RTC_OK
    
        ##
        #
        # The execution action that is invoked periodically
        # former rtc_active_do()
        #
        # @param ec_id target ExecutionContext Id
        #
        # @return RTC::ReturnCode_t
        #
        #
    def onExecute(self, ec_id):

        if self._rgbdCameraImageIn.isNew():
            m_color_data = self._rgbdCameraImageIn.read()
            print "kitayo"

            for i in range(0, *height):
                for j in range(0, *width):
                    index = (i * array(width) + j) * 3
                    m_img[h, w][2] = m_color_data.data.cameraImage.image.raw_data[index + 2] # b
                    m_img[h, w][1] = self._rgbdCameraImageIn.data.cameraImage.image.raw_data[index + 1] # g
                    m_img[h, w][0] = self._rgbdCameraImageIn.data.cameraImage.image.raw_data[index + 0] # r
            cv2.imshow('image', m_img)

            
        width = self._frame_width
        height = self._frame_height
        channels = 3

    
        return RTC.RTC_OK
    
    #   ##
    #   #
    #   # The aborting action when main logic error occurred.
    #   # former rtc_aborting_entry()
    #   #
    #   # @param ec_id target ExecutionContext Id
    #   #
    #   # @return RTC::ReturnCode_t
    #   #
    #   #
    #def onAborting(self, ec_id):
    #
    #   return RTC.RTC_OK
    
    #   ##
    #   #
    #   # The error action in ERROR state
    #   # former rtc_error_do()
    #   #
    #   # @param ec_id target ExecutionContext Id
    #   #
    #   # @return RTC::ReturnCode_t
    #   #
    #   #
    #def onError(self, ec_id):
    #
    #   return RTC.RTC_OK
    
    #   ##
    #   #
    #   # The reset action that is invoked resetting
    #   # This is same but different the former rtc_init_entry()
    #   #
    #   # @param ec_id target ExecutionContext Id
    #   #
    #   # @return RTC::ReturnCode_t
    #   #
    #   #
    #def onReset(self, ec_id):
    #
    #   return RTC.RTC_OK
    
    #   ##
    #   #
    #   # The state update action that is invoked after onExecute() action
    #   # no corresponding operation exists in OpenRTm-aist-0.2.0
    #   #
    #   # @param ec_id target ExecutionContext Id
    #   #
    #   # @return RTC::ReturnCode_t
    #   #

    #   #
    #def onStateUpdate(self, ec_id):
    #
    #   return RTC.RTC_OK
    
    #   ##
    #   #
    #   # The action that is invoked when execution context's rate is changed
    #   # no corresponding operation exists in OpenRTm-aist-0.2.0
    #   #
    #   # @param ec_id target ExecutionContext Id
    #   #
    #   # @return RTC::ReturnCode_t
    #   #
    #   #
    #def onRateChanged(self, ec_id):
    #
    #   return RTC.RTC_OK
    



def RGBDcameraViewerInit(manager):
    profile = OpenRTM_aist.Properties(defaults_str=rgbdcameraviewer_spec)
    manager.registerFactory(profile,
                            RGBDcameraViewer,
                            OpenRTM_aist.Delete)

def MyModuleInit(manager):
    RGBDcameraViewerInit(manager)

    # Create a component
    comp = manager.createComponent("RGBDcameraViewer")

def main():
    mgr = OpenRTM_aist.Manager.init(sys.argv)
    mgr.setModuleInitProc(MyModuleInit)
    mgr.activateManager()
    mgr.runManager()

if __name__ == "__main__":
    main()

