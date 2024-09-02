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
            i, j = i + 1, j + 1
        else:
            result = a[i] + result
            i, j = i + 1, j + 1
    return result + b[j:]
