from typing import List


def string_xor(a: str, b: str) -> str:
    """ Input are two strings a and b consisting only of 1s and 0s.
    Perform binary XOR on these inputs and return result also as a string.
    >>> string_xor('010', '110')
    '100'
    """
    n, m = len(a), len(b)
    if n > m:
        return string_xor(b, a)
    return ''.join(
        str(int(a[i]) ^ int(b[i])) for i in range(m)
    )

