from typing import List


def string_xor(a: str, b: str) -> str:
    """ Input are two strings a and b consisting only of 1s and 0s.
    Perform binary XOR on these inputs and return result also as a string.
    >>> string_xor('010', '110')
    '100'
    """
    if len(a) > len(b):
        tmp = b
        b = a
        a = tmp
    res = ""
    for i in range(len(b)):
        if a[i] == b[i]:
            res += "0"
        else:
            res += "1"
    return res

