from typing import List


def string_xor(a: str, b: str) -> str:
    """ Input are two strings a and b consisting only of 1s and 0s.
    Perform binary XOR on these inputs and return result also as a string.
    >>> string_xor('010', '110')
    '100'
    """
    xored_str = ''
    for (a_bit, b_bit) in zip(a, b):
        xored_bit = a_bit ^ b_bit
        xored_str += str(xored_bit)
    return xored_str

