from typing import List


def string_xor(a: str, b: str) -> str:
    """ Input are two strings a and b consisting only of 1s and 0s.
    Perform binary XOR on these inputs and return result also as a string.
    >>> string_xor('010', '110')
    '100'
    """
    a_chars = a.translate(str.maketrans('01', '10'))
    b_chars = b.translate(str.maketrans('01', '10'))
    if len(a_chars)!= len(b_chars):
        raise ValueError(f"Strings do not have same length: {a}, {b}")
    return ''.join(chr(ord(a) ^ ord(b)) for a, b in zip(a_chars, b_chars))

