from typing import List


def string_xor(a: str, b: str) -> str:
    """ Input are two strings a and b consisting only of 1s and 0s.
    Perform binary XOR on these inputs and return result also as a string.
    >>> string_xor('010', '110')
    '100'
    """
    str1 = int(a, 2) ^ int(b, 2)
    a_bin = bin(str1)
    a_bin = a_bin[2:]
    str1 = '0' * (len(a) - len(a_bin)) + a_bin
    return str1

