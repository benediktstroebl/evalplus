from typing import List


def string_xor(a: str, b: str) -> str:
    """ Input are two strings a and b consisting only of 1s and 0s.
    Perform binary XOR on these inputs and return result also as a string.
    >>> string_xor('010', '110')
    '100'
    """
    # Make sure the strings are the same length
    if len(a)!= len(b):
        raise ValueError('a and b must be the same length')
    return ''.join(str((int(x) ^ int(y))) for x, y in zip(a, b))

