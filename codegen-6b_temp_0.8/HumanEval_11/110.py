from typing import List


def string_xor(a: str, b: str) -> str:
    """ Input are two strings a and b consisting only of 1s and 0s.
    Perform binary XOR on these inputs and return result also as a string.
    >>> string_xor('010', '110')
    '100'
    """
    xor = lambda c1, c2: '0' if c1 == c2 else '1'
    b_to_int = lambda c: int(c)
    return ''.join(map(xor, b_to_int(a[i]), b_to_int(b[i])))

