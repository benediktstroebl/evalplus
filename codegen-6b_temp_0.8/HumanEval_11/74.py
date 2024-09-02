from typing import List


def string_xor(a: str, b: str) -> str:
    """ Input are two strings a and b consisting only of 1s and 0s.
    Perform binary XOR on these inputs and return result also as a string.
    >>> string_xor('010', '110')
    '100'
    """
    res = ''
    for index, char in enumerate(a):
        if char == '0' and b[index] == '1':
            res += '1'
        elif char == '1' and b[index] == '0':
            res += '0'
        else:
            res += '0'
    return res

