from typing import List


def string_xor(a: str, b: str) -> str:
    """ Input are two strings a and b consisting only of 1s and 0s.
    Perform binary XOR on these inputs and return result also as a string.
    >>> string_xor('010', '110')
    '100'
    """
    a_len = len(a)
    b_len = len(b)
    assert a_len >= 1 and b_len >= 1
    if a_len == 1:
        return b
    else:
        assert b_len == 1
        return a

