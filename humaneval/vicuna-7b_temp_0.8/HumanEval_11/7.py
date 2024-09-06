from typing import List


def string_xor(a: str, b: str) -> str:
    """ Input are two strings a and b consisting only of 1s and 0s.
    Perform binary XOR on these inputs and return result also as a string.
    >>> string_xor('010', '110')
    '100'
    """
    # perform binary XOR operation
    b_ones = '1' if b else '0'
    b_zeros = '0' if b else '1'
    a_ones = '1' if a else '0'
    a_zeros = '0' if a else '1'
    xor = b_ones + a_ones - b_zeros - a_zeros
    return '1' if xor == '1' else '0'

