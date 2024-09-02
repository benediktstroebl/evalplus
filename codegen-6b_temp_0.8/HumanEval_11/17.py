from typing import List


def string_xor(a: str, b: str) -> str:
    """ Input are two strings a and b consisting only of 1s and 0s.
    Perform binary XOR on these inputs and return result also as a string.
    >>> string_xor('010', '110')
    '100'
    """
    assert len(a) == len(b)
    a = list(a)
    b = list(b)
    return "".join([str(int(a_bit) ^ int(b_bit)) for a_bit, b_bit in zip(a, b)])

