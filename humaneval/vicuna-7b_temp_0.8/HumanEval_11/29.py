from typing import List


def string_xor(a: str, b: str) -> str:
    """ Input are two strings a and b consisting only of 1s and 0s.
    Perform binary XOR on these inputs and return result also as a string.
    >>> string_xor('010', '110')
    '100'
    """
    # Convert each character to binary
    a_bin = bin(ord(a[i]) for i in range(len(a)))
    b_bin = bin(ord(b[i]) for i in range(len(b)))

    # Perform XOR operation on binary strings
    xor_bin = bin(int(a_bin[::-1], 2) ^ int(b_bin[::-1], 2))

    # Convert result back to string
    xor_str = ''.join(str(ord(c)) for c in xor_bin)

    return xor_str
