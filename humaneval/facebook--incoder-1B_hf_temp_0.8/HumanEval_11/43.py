from typing import List


def string_xor(a: str, b: str) -> str:
    """ Input are two strings a and b consisting only of 1s and 0s.
    Perform binary XOR on these inputs and return result also as a string.
    >>> string_xor('010', '110')
    '100'
    """
    a_bytes = [int(b[i:i + 2], 2) for i in range(a)]
    b_bytes = [int(b[i:i + 2], 2) for i in range(a)]

    return ''.join([chr(a ^ b) for a, b in zip(a_bytes, b_bytes)])

