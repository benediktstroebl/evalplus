from typing import List


def string_xor(a: str, b: str) -> str:
    """ Input are two strings a and b consisting only of 1s and 0s.
    Perform binary XOR on these inputs and return result also as a string.
    >>> string_xor('010', '110')
    '100'
    """
    # convert to binary
    a_bin = '0' + a
    b_bin = '0' + b
    # perform binary XOR
    xor = bin(int(a_bin, 2) ^ int(b_bin, 2))
    # convert back to string
    xor_str = ''.join(str(x) for x in xor)
    return xor_str

