from typing import List


def string_xor(a: str, b: str) -> str:
    """ Input are two strings a and b consisting only of 1s and 0s.
    Perform binary XOR on these inputs and return result also as a string.
    >>> string_xor('010', '110')
    '100'
    """
    char_set = set(chr(i) for i in range(ord('a'), ord('z') + 1))
    return ''.join(c ^ n for c, n in zip(char_set, (a, b)))

