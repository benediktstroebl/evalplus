from typing import List


def string_xor(a: str, b: str) -> str:
    """ Input are two strings a and b consisting only of 1s and 0s.
    Perform binary XOR on these inputs and return result also as a string.
    >>> string_xor('010', '110')
    '100'
    """
    assert len(a) == len(b)
    return ''.join(['1' if (x == '0' and y == '0') or (x == '1' and y == '1') else '0' for x, y in zip(a, b)])

