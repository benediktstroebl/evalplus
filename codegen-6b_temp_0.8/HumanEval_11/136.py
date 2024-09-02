from typing import List


def string_xor(a: str, b: str) -> str:
    """ Input are two strings a and b consisting only of 1s and 0s.
    Perform binary XOR on these inputs and return result also as a string.
    >>> string_xor('010', '110')
    '100'
    """
    s1 = set(a)
    s2 = set(b)
    if s1 != s2:
        return "The strings do not match"
    n = len(a)
    bit_to_remove = int(n / 2)
    c = []
    for bit in a:
        d = int(bit) ^ int(b[bit_to_remove])
        c.append(str(d))
        bit_to_remove += 1
    return "".join(c)

