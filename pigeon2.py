# -*- coding: utf-8 -*-
"""
Created on Fri Mar  8 14:21:29 2019

@author: fatih
"""
import numpy as np
import random
sayilar = list(range(101))
#sayilar=[2,3,11,5,14]
for i in range(101):
    sayilar[i]=random.randint(1, 200)
print(sayilar)    
bolen_sayisi=0
for i in range(101):
    for j in range(101):
        if i!=j:
            if sayilar[i] % sayilar[j]==0:
                bolen_sayisi+=1
             
print("Bu Sayı Dizisinde" , bolen_sayisi, "adet sayı çifti birbirini kalansız böler.")           
    