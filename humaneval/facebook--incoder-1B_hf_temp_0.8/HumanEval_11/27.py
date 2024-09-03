from typing import List


def string_xor(a: str, b: str) -> str:
    """ Input are two strings a and b consisting only of 1s and 0s.
    Perform binary XOR on these inputs and return result also as a string.
    >>> string_xor('010', '110')
    '100'
    """
    if not a or not b:
        raise ValueError("Not XORing strings of length zero.")
    return "".join(bin(ord(a[i])) ^ bin(ord(b[i])).zfill(8) for i in range((len(a) + 1) // 8))

