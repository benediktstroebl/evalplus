from typing import List


def string_xor(a: str, b: str) -> str:
    """ Input are two strings a and b consisting only of 1s and 0s.
    Perform binary XOR on these inputs and return result also as a string.
    >>> string_xor('010', '110')
    '100'
    """
    if len(a) != len(b):
        return ''
    result = ''
    for i in range(len(a)):
        if a[i] != b[i]:
            result += str(int(a[i], 2) ^ int(b[i], 2))
    return result
