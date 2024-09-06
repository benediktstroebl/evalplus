import unittest
def eat(n, need, rem):
    cath = n + need
    lef = rem - cath
    if lef < 0:
        cath = rem
        lef = 0
    return [cath, lef]