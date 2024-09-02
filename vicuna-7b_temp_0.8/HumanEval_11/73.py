from typing import List


def string_xor(a: str, b: str) -> str:
    """ Input are two strings a and b consisting only of 1s and 0s.
    Perform binary XOR on these inputs and return result also as a string.
    >>> string_xor('010', '110')
    '100'
    """
    a_ones = '0' * len(a)
    b_ones = '0' * len(b)
    a_zeros = '1' * len(a)
    b_zeros = '1' * len(b)
    result = a_ones + b_zeros + a_zeros + b_zeros
    return result.rjust(len(a) + len(b) + 1, '0')

