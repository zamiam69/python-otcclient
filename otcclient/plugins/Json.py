#!/usr/bin/env python
# -*- coding: utf-8 -*-

# This file is part of OTC Tool released under MIT license.
# Copyright (C) 2016 T-systems Kurt Garloff, Zsolt Nagy 

from otcclient.core.OtcConfig import OtcConfig 
from otcclient.core.otcpluginbase import otcpluginbase
from otcclient.utils import utils_output 

class Json(otcpluginbase):
    
    def otctype(self):
        return "utils_output" 
    
    @staticmethod
    def handleQuery(result):
        utils_output.handleQuery(result, OtcConfig.QUERY)
                
    @staticmethod
    def print_output(respjson, **kwargs):
        
        if isinstance(respjson, (str, unicode)):
            if len(respjson.strip()) == 0:
                return

        utils_output.printJsonTableTransverse(respjson, "json", None)