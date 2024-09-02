from typing import List


def string_xor(a: str, b: str) -> str:
    """ Input are two strings a and b consisting only of 1s and 0s.
    Perform binary XOR on these inputs and return result also as a string.
    >>> string_xor('010', '110')
    '100'
    """
    res = ''
    i = 0
    while i < len(a) or i < len(b):
        if i < len(a) and i < len(b):
            if a[i] == b[i]:
                res += '0'
            else:
                res += '1'
        elif i < len(a):
            res += a[i]
        elif i < len(b):
            res += b[i]
        i += 1
    return res

