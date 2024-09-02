from typing import List


def string_xor(a: str, b: str) -> str:
    """ Input are two strings a and b consisting only of 1s and 0s.
    Perform binary XOR on these inputs and return result also as a string.
    >>> string_xor('010', '110')
    '100'
    """
    a = list(map(int, list(a)))
    b = list(map(int, list(b)))
    return "".join(map(str, map(lambda x, y: x ^ y, a, b)))

