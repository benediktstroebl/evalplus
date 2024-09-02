from typing import List


def string_xor(a: str, b: str) -> str:
    """ Input are two strings a and b consisting only of 1s and 0s.
    Perform binary XOR on these inputs and return result also as a string.
    >>> string_xor('010', '110')
    '100'
    """
    b = '1' * len(a)  # copy b to get a same length string
    c = 0
    for i in range(len(a)):
        if a[i] == '1':
            c ^= 1
        b[i] = '1' if c == 1 else '0'
    return b

