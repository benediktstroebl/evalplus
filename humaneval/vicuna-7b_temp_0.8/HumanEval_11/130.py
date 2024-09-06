from typing import List


def string_xor(a: str, b: str) -> str:
    """ Input are two strings a and b consisting only of 1s and 0s.
    Perform binary XOR on these inputs and return result also as a string.
    >>> string_xor('010', '110')
    '100'
    """
    a_ones = sum(1 for char in a if char == '1')
    b_ones = sum(1 for char in b if char == '1')
    a_zeros = sum(1 for char in a if char == '0')
    b_zeros = sum(1 for char in b if char == '0')
    return '1' * (a_ones + b_ones) + '0' * (a_zeros + b_zeros)
