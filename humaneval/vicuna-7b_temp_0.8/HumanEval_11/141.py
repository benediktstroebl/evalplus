from typing import List


def string_xor(a: str, b: str) -> str:
    """ Input are two strings a and b consisting only of 1s and 0s.
    Perform binary XOR on these inputs and return result also as a string.
    >>> string_xor('010', '110')
    '100'
    """
    result = ''
    i = j = 0
    while i < len(a) and j < len(b):
        if a[i] == b[j]:
            i += 1
            j += 1
            continue
        elif a[i] == '0':
            result = '1' + result
        else:
            result = '0' + result
        i += 1
        j += 1
    return result + (len(a) + len(b) - i - j) % 2

