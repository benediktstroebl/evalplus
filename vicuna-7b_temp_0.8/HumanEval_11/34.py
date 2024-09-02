from typing import List


def string_xor(a: str, b: str) -> str:
    """ Input are two strings a and b consisting only of 1s and 0s.
    Perform binary XOR on these inputs and return result also as a string.
    >>> string_xor('010', '110')
    '100'
    """
    # convert to binary
    ba = bin(a)[2:] * 2 + bin(b)[2:]
    # perform xor
    return ''.join(char ^ (ord(char) if ord(char) < 128 else 0x7f) for char in ba)
