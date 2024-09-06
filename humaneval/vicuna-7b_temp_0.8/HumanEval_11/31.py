from typing import List


def string_xor(a: str, b: str) -> str:
    """ Input are two strings a and b consisting only of 1s and 0s.
    Perform binary XOR on these inputs and return result also as a string.
    >>> string_xor('010', '110')
    '100'
    """
    # converting each character to binary
    a_bin = bin(ord(a[0])) + bin(ord(a[1])) + bin(ord(a[2]))
    b_bin = bin(ord(b[0])) + bin(ord(b[1])) + bin(ord(b[2]))

    # performing binary XOR
    xor_bin = a_bin + b_bin

    # converting binary back to string
    xor = bin(int(xor_bin, 2))

    return xor.decode('utf-8') if type(xor) == bytes else xor
