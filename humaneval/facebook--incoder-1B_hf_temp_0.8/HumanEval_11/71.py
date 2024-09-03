from typing import List


def string_xor(a: str, b: str) -> str:
    """ Input are two strings a and b consisting only of 1s and 0s.
    Perform binary XOR on these inputs and return result also as a string.
    >>> string_xor('010', '110')
    '100'
    """
    a = ''.join(str(a)).lower()
    b = ''.join(str(b)).lower()
    return ''.join(
        chr(ord(a) ^ ord(b)) if a!= b else a if a == b else b
        for a in a
    )

