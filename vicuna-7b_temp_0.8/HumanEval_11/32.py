from typing import List


def string_xor(a: str, b: str) -> str:
    """ Input are two strings a and b consisting only of 1s and 0s.
    Perform binary XOR on these inputs and return result also as a string.
    >>> string_xor('010', '110')
    '100'
    """
    a = a.translate(str.maketrans('', '', '1'))
    b = b.translate(str.maketrans('', '', '1'))
    return a.join(b)

