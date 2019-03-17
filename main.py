#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 16 17:18:19 2019

@author: shriganeshkolhe
"""

import methods

j = methods.by_zipcode("443404").to_dict()
print(j)