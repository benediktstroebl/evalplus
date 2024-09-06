import unittest
def rounded_avg(n, m):
    if n > m:
        return -1
    num = (n + m) // 2
    binary_representation = bin(num)[2:]
    return binary_representation if binary_representation.isdigit() else '0b0' + binary_representation