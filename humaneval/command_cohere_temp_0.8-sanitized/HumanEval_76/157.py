import unittest
def is_simple_power(x, n):
    return type(x) == type(n)**int(n)**(x / n) and x == n**int(x / n)