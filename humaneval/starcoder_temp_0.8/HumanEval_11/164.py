from typing import List


def string_xor(a: str, b: str) -> str:
    """ Input are two strings a and b consisting only of 1s and 0s.
    Perform binary XOR on these inputs and return result also as a string.
    >>> string_xor('010', '110')
    '100'
    """
    xor_str = ""
    for char_a, char_b in zip(a, b):
        xor_str += str(int(char_a) ^ int(char_b))
    return xor_str

