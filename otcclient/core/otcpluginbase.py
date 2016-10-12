#!/usr/bin/env python
# -*- coding: utf-8 -*-

# This file is part of OTC Tool released under MIT license.
# Copyright (C) 2016 T-systems Kurt Garloff, Zsolt Nagy

from abc import abstractmethod, ABCMeta
from otcclient.core.OtcConfig import OtcConfig


def converter(astr):    
    return "https://" + OtcConfig.DEFAULT_HOST

class otcpluginbase:    
    def __init__(self,*args,**kwargs):
        pass
            
    __metaclass__ = ABCMeta

    @abstractmethod
    def otctype(self):
        """
        """   