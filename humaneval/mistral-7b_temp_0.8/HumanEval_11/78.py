from typing import List


def string_xor(a: str, b: str) -> str:
    """ Input are two strings a and b consisting only of 1s and 0s.
    Perform binary XOR on these inputs and return result also as a string.
    >>> string_xor('010', '110')
    '100'
    """
    # raise NotImplementedError
    res = ""
    a_len = len(a)
    b_len = len(b)
    xor = 0
    for i in range(a_len):
        xor = a[i] ^ b[i]
        res += str(xor)
    return res

