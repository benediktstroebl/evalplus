from typing import List


def string_xor(a: str, b: str) -> str:
    """ Input are two strings a and b consisting only of 1s and 0s.
    Perform binary XOR on these inputs and return result also as a string.
    >>> string_xor('010', '110')
    '100'
    """
    xor_str = ''
    for a_digit, b_digit in zip(a, b):
        if a_digit == '0':
            xor_str += '1'
        else:
            xor_str += '0'
    for i in range(len(b)):
        if b[i] == '0':
            xor_str += '1'
        else:
            xor_str += '0'
    return xor_str

