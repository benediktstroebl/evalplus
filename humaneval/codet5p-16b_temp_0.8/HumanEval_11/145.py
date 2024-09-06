from typing import List


def string_xor(a: str, b: str) -> str:
    """ Input are two strings a and b consisting only of 1s and 0s.
    Perform binary XOR on these inputs and return result also as a string.
    >>> string_xor('010', '110')
    '100'
    """

    # convert strs to binary
    binary_a = a.encode('utf-8')
    binary_b = b.encode('utf-8')
    # perform xor on the binary strings
    binary_xor = bytes([b1 ^ b2 for b1, b2 in zip(binary_a, binary_b)])
    # convert the result back to str
    return binary_xor.decode('utf-8')

