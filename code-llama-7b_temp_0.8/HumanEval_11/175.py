from typing import List


def string_xor(a: str, b: str) -> str:
    """ Input are two strings a and b consisting only of 1s and 0s.
    Perform binary XOR on these inputs and return result also as a string.
    >>> string_xor('010', '110')
    '100'
    """
    a, b = a.replace('0', ''), b.replace('0', '')
    a, b = a.replace('1', 'T'), b.replace('1', 'T')
    return ''.join(map(lambda x: str(not x[0] and x[1]), zip(a, b)))

