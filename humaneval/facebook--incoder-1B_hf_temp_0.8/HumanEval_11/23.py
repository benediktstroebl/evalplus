from typing import List


def string_xor(a: str, b: str) -> str:
    """ Input are two strings a and b consisting only of 1s and 0s.
    Perform binary XOR on these inputs and return result also as a string.
    >>> string_xor('010', '110')
    '100'
    """
    a_chars = set(map(ord, a))
    b_chars = set(map(ord, b))
    return ''.join((c_chars[a_chars.intersection(b_chars)] ^ c_chars[b_chars.intersection(a)]) for c in a)

