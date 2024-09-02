from typing import List


def string_xor(a: str, b: str) -> str:
    """ Input are two strings a and b consisting only of 1s and 0s.
    Perform binary XOR on these inputs and return result also as a string.
    >>> string_xor('010', '110')
    '100'
    """
    xor = ''
    a_index = 0
    b_index = 0
    while a_index < len(a) and b_index < len(b):
        if a[a_index] == b[b_index]:
            xor += '0'
        else:
            xor += '1'
        a_index += 1
        b_index += 1
    while a_index < len(a):
        xor += a[a_index]
        a_index += 1
    while b_index < len(b):
        xor += b[b_index]
        b_index += 1
    return xor

