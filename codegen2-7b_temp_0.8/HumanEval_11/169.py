from typing import List


def string_xor(a: str, b: str) -> str:
    """ Input are two strings a and b consisting only of 1s and 0s.
    Perform binary XOR on these inputs and return result also as a string.
    >>> string_xor('010', '110')
    '100'
    """
    assert len(a) == len(b)
    assert all(c == '1' for c in a)
    assert all(c == '1' for c in b)
    return ''.join(c * 2 for c in a ^ b
