from typing import List


def string_xor(a: str, b: str) -> str:
    """ Input are two strings a and b consisting only of 1s and 0s.
    Perform binary XOR on these inputs and return result also as a string.
    >>> string_xor('010', '110')
    '100'
    """
    char_a = set(a)
    char_b = set(b)
    if len(char_a) != len(char_b):
        return ''
    return ''.join(['0' if c not in char_b else '1' for c in a])

