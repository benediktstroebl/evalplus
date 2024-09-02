from typing import List


def string_xor(a: str, b: str) -> str:
    """ Input are two strings a and b consisting only of 1s and 0s.
    Perform binary XOR on these inputs and return result also as a string.
    >>> string_xor('010', '110')
    '100'
    """
    if len(a) != len(b):
        raise ValueError("a and b should be of same length")
    a_int = int(a, base=2)
    b_int = int(b, base=2)
    xor = a_int ^ b_int
    return format(xor, "b")

