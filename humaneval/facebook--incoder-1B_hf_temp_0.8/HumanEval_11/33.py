from typing import List


def string_xor(a: str, b: str) -> str:
    """ Input are two strings a and b consisting only of 1s and 0s.
    Perform binary XOR on these inputs and return result also as a string.
    >>> string_xor('010', '110')
    '100'
    """
    a_chars = list(map(int, a.split('0')))
    b_chars = list(map(int, b.split('0')))
    return "".join(chr(ord(x) ^ ord(y)) for x, y in zip(a_chars, b_chars))

