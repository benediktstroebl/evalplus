from typing import List


def string_xor(a: str, b: str) -> str:
    """ Input are two strings a and b consisting only of 1s and 0s.
    Perform binary XOR on these inputs and return result also as a string.
    >>> string_xor('010', '110')
    '100'
    """
    a, b = [i if i else '0' for i in (a, b)]
    return ''.join(chr(int(c, 2) ^ int(d, 2)) if c else '0' if d == '1' else '1' for c, d in zip(a, b))

