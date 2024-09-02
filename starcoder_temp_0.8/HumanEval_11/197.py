from typing import List


def string_xor(a: str, b: str) -> str:
    """ Input are two strings a and b consisting only of 1s and 0s.
    Perform binary XOR on these inputs and return result also as a string.
    >>> string_xor('010', '110')
    '100'
    """
    a = bin(int(a, 2))
    b = bin(int(b, 2))
    a = a[2:]
    b = b[2:]

    l1 = max(len(a), len(b))
    l2 = min(len(a), len(b))

    a = a.zfill(l1)
    b = b.zfill(l1)

    xor = ""
    for i in range(l2):
        if a[i] == b[i]:
            xor = xor + "0"
        else:
            xor = xor + "1"

    return xor
