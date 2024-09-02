from typing import List


def string_xor(a: str, b: str) -> str:
    """ Input are two strings a and b consisting only of 1s and 0s.
    Perform binary XOR on these inputs and return result also as a string.
    >>> string_xor('010', '110')
    '100'
    """
    result = ''
    i = 0
    while i < len(a) and i < len(b):
        if a[i] == b[i]:
            result += a[i]
            i += 1
        elif a[i] == '0':
            while b[i] == '0':
                i += 1
            result += '1'
            i += 1
        else:
            while b[i] == '1':
                i += 1
            result += '0'
            i += 1
    return result

