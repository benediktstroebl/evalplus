from typing import List


def string_xor(a: str, b: str) -> str:
    """ Input are two strings a and b consisting only of 1s and 0s.
    Perform binary XOR on these inputs and return result also as a string.
    >>> string_xor('010', '110')
    '100'
    """
    if not (a and b) or len(a) != len(b):
        raise ValueError('a and b must be of same length')
    return ''.join([str(ord(a) ^ ord(b)) for a, b in zip(a, b)])

