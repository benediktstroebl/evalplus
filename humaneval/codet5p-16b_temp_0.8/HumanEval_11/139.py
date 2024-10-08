from typing import List


def string_xor(a: str, b: str) -> str:
    """ Input are two strings a and b consisting only of 1s and 0s.
    Perform binary XOR on these inputs and return result also as a string.
    >>> string_xor('010', '110')
    '100'
    """

    if len(a)!= len(b):
        raise ValueError(f"Lengths of strings do not match. Length of string a: {len(a)}, length of string b: {len(b)}")

    return ''.join([str(int(a[i]) ^ int(b[i])) for i in range(len(a))])

