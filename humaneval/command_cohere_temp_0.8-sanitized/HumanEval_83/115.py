import unittest
def starts_one_ends(n):
    tot = 0
    for i in range(n):
        num = 1
        for j in range(n-i-1):
            num = num*10 + 1
            tot += num <= 1000000
    return tot