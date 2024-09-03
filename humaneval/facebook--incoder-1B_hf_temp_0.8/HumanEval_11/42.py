from typing import List


def string_xor(a: str, b: str) -> str:
    """ Input are two strings a and b consisting only of 1s and 0s.
    Perform binary XOR on these inputs and return result also as a string.
    >>> string_xor('010', '110')
    '100'
    """
    # use xor to calculate xor of string a and string b
    xor_result = int(''.join([a ^ b for b in a]), 2)
    return bin(xor_result)[2:].zfill(len(bin(a))).lstrip("0b")

