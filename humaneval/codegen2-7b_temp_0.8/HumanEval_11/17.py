from typing import List


def string_xor(a: str, b: str) -> str:
    """ Input are two strings a and b consisting only of 1s and 0s.
    Perform binary XOR on these inputs and return result also as a string.
    >>> string_xor('010', '110')
    '100'
    """
    assert len(a) == len(b)
    assert all(c in '01' for c in a)
    assert all(c in '01' for c in b)
    return "".join("{0:b}".format(int(c) ^ int(d)) for c, d in zip(a, b))
