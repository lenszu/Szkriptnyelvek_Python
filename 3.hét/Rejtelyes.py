#! /usr/bin/env python3
from curses.ascii import islower
import sys
import os
import math
import random
import time

#A papír túloldalán csupán ennyi áll: "K → M, O → Q, E → G". 

def main():
    s="""Cbcq Dgyk!

        Dmeybh kce cew yrwyg hmrylyaqmr:
        rylsjb kce y Nwrfml npmepykmxyqg lwcjtcr!

    Aqmimjjyi:

    Ynyb
    """
    result=""""""
    for i in range(len(s)):
        if s[i]=="K" or s[i]=="k":
            if islower(s[i]):
                result+="m"
            else:
                result+="M"
        elif s[i]=="O" or s[i]=="o":
            if islower(s[i]):
                result+="q"
            else:
                result+="Q"
        elif s[i]=="E" or s[i]=="e":
            if islower(s[i]):
                result+="g"
            else:
                result+="G"
        else:
            result+=s[i]
            
        print(result)


if __name__ == '__main__':
    main()