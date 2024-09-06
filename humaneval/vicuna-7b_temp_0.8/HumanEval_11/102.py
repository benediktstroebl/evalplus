from typing import List


def string_xor(a: str, b: str) -> str:
    """ Input are two strings a and b consisting only of 1s and 0s.
    Perform binary XOR on these inputs and return result also as a string.
    >>> string_xor('010', '110')
    '100'
    """
    a_ones = [i == '1' for i in a]
    b_ones = [i == '1' for i in b]
    a_zeros = [i == '0' for i in a]
    b_zeros = [i == '0' for i in b]
    xor_mask = (~a_ones) & (~b_ones)
    a_xor = '1' * len(a)
    b_xor = '1' * len(b)
    xor = a_xor + b_xor + '0' * (len(a_xor) + len(b_xor))[1:-1]
    return '0' if any(xor_mask) else xor
