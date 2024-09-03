from typing import List


def string_xor(a: str, b: str) -> str:
    """ Input are two strings a and b consisting only of 1s and 0s.
    Perform binary XOR on these inputs and return result also as a string.
    >>> string_xor('010', '110')
    '100'
    """
    if a == '' and b == '':
        return '0'
    elif a == '':
        return b
    elif b == '':
        return a
    return ''.join(map(''.xor, zip(a, b)))

