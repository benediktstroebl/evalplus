from typing import List


def string_xor(a: str, b: str) -> str:
    """ Input are two strings a and b consisting only of 1s and 0s.
    Perform binary XOR on these inputs and return result also as a string.
    >>> string_xor('010', '110')
    '100'
    """
    if not a or not b:
        return b
    elif len(a) == len(b):
        return ''.join(a[i] ^ b[i] for i in range(len(a)))
    else:
        return '0' * len(a)

