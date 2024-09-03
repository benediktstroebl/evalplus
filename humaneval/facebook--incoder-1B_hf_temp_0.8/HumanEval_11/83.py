from typing import List


def string_xor(a: str, b: str) -> str:
    """ Input are two strings a and b consisting only of 1s and 0s.
    Perform binary XOR on these inputs and return result also as a string.
    >>> string_xor('010', '110')
    '100'
    """
    a, b = str(a), str(b)
    if len(a)!= len(b):
        raise ValueError("Inputs must be same length.")
    i = 0
    j = 0
    while i < len(a) and j < len(b):
        if a[i] ^ b[j]:
            j += 1
        else:
            i += 1
    return str(j) if j < len(b) else str(i) if i < len(a) else ""

