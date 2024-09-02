from typing import List


def string_xor(a: str, b: str) -> str:
    """ Input are two strings a and b consisting only of 1s and 0s.
    Perform binary XOR on these inputs and return result also as a string.
    >>> string_xor('010', '110')
    '100'
    """
    # if a and b are of different length pad the shorter one with zeroes
    if len(a) < len(b):
        a = a.ljust(len(b), '0')
    elif len(b) < len(a):
        b = b.ljust(len(a), '0')

    return ''.join(map(lambda x: '1' if x[0] != x[1] else '0', zip(a, b)))

