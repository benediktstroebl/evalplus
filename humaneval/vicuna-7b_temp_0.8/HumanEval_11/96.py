from typing import List


def string_xor(a: str, b: str) -> str:
    """ Input are two strings a and b consisting only of 1s and 0s.
    Perform binary XOR on these inputs and return result also as a string.
    >>> string_xor('010', '110')
    '100'
    """
    # convert to binary
    a_bin = ''.join(str(x) for x in a)
    b_bin = ''.join(str(x) for x in b)

    # perform binary XOR
    xor_bin = ''.join(~(a_bin[i] ^ b_bin[i]) for i in range(len(a_bin)))

    # convert back to string
    xor_str = ''.join(str(x) for x in xor_bin)

    return xor_str
