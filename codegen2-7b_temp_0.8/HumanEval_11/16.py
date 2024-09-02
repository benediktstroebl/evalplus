from typing import List


def string_xor(a: str, b: str) -> str:
    """ Input are two strings a and b consisting only of 1s and 0s.
    Perform binary XOR on these inputs and return result also as a string.
    >>> string_xor('010', '110')
    '100'
    """
    a_xor_b = bin(int(a, 2) ^ int(b, 2))[2:]
    return "".join(map(lambda c: "1" if c == "0" else "0", a_xor_b
