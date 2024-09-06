from typing import List


def string_xor(a: str, b: str) -> str:
    """ Input are two strings a and b consisting only of 1s and 0s.
    Perform binary XOR on these inputs and return result also as a string.
    >>> string_xor('010', '110')
    '100'
    """
    xor = 0
    for i, char in enumerate(a):
        xor ^= ord(char)
        if b[i] == '1':
            xor ^= 1
    return xor.to_bytes(1, byteorder='big').hex
