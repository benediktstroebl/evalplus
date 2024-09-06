from typing import List


def string_xor(a: str, b: str) -> str:
    """ Input are two strings a and b consisting only of 1s and 0s.
    Perform binary XOR on these inputs and return result also as a string.
    >>> string_xor('010', '110')
    '100'
    """
    # Convert each string to binary and take XOR
    a_bin = ''.join(str(x) for x in a)
    b_bin = ''.join(str(x) for x in b)
    return ''.join(chr(x) for x in bin(int(a_bin, 2)) ^ bin(int(b_bin, 2)))

