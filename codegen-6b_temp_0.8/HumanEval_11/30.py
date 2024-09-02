from typing import List


def string_xor(a: str, b: str) -> str:
    """ Input are two strings a and b consisting only of 1s and 0s.
    Perform binary XOR on these inputs and return result also as a string.
    >>> string_xor('010', '110')
    '100'
    """
    a, b = a.encode(), b.encode()
    return bytes([a_b ^ b_b for a_b, b_b in zip(a, b)]).decode()

