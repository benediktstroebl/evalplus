import unittest
def make_a_pile(n):
    if n == 1:
        return [n]
    else:
        return [n] + odd_even(n + 1)
def odd_even(number):
    if number % 2 == 0:
        return [number]
    else:
        return [number, number + 2]