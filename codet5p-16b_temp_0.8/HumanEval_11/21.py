from typing import List


def string_xor(a: str, b: str) -> str:
    """ Input are two strings a and b consisting only of 1s and 0s.
    Perform binary XOR on these inputs and return result also as a string.
    >>> string_xor('010', '110')
    '100'
    """

    a = ''.join(['0' if chr(c) == '1' else '1' for c in a])
    b = ''.join(['0' if chr(c) == '1' else '1' for c in b])
    return bin(int(a, 2) ^ int(b, 2))[2:].zfill(len(a))

