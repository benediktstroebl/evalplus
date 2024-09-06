from typing import List


def string_xor(a: str, b: str) -> str:
    """ Input are two strings a and b consisting only of 1s and 0s.
    Perform binary XOR on these inputs and return result also as a string.
    >>> string_xor('010', '110')
    '100'
    """
    # Convert both strings to binary
    a = ''.join(map(str, a))
    b = ''.join(map(str, b))

    # Perform binary XOR on both strings
    xor = 0
    for i in range(len(a)):
        xor ^= bin(int(a[i], 2)) ^ bin(int(b[i], 2))

    # Convert the result back to a string
    return ''.join(map(str, [x for x in xor if x == 1])) or '0'
