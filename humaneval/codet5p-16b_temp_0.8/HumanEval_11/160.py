from typing import List


def string_xor(a: str, b: str) -> str:
    """ Input are two strings a and b consisting only of 1s and 0s.
    Perform binary XOR on these inputs and return result also as a string.
    >>> string_xor('010', '110')
    '100'
    """

    if len(a) > len(b):
        b = '0' * (len(a) - len(b)) + b
    elif len(b) > len(a):
        a = '0' * (len(b) - len(a)) + a

    return ''.join(str(int(a[i]) ^ int(b[i])))

