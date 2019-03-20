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


# Güvercin Yuvası prensibine göre 1 ile 200 arasında seçilen 101 sayıdan en az 2 tanesinin birbirini tam böldüğünü gösterir.
bolen_sayisi1=0
a=0
b=0
n=0
k=0
for i in range(101):
    a=sayilar[i]
    while a%2==0:
        n+=1
        a/=2
    for j in range(101):
        if i!=j:
            b=sayilar[j]
            while b%2==0:
                k+=1
                b/=2
            if sayilar[i]>sayilar[j] and a==b:
                bolen_sayisi1+=1
print ("Bu sayı dizisinde en az ",bolen_sayisi1," sayı birbirini tam bölmektedir")



#Birbirini tam bölen sayı adedini tam olarak bulur.
bolen_sayisi2=0
for i in range(101):
    for j in range(101):
        if i!=j:
            if sayilar[i] % sayilar[j]==0:
                bolen_sayisi2+=1
print("Bu Sayı Dizisinde" , bolen_sayisi2, "adet sayı çifti birbirini kalansız böler.") 