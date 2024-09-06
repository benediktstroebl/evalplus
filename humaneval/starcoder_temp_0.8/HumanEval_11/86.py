from typing import List


def string_xor(a: str, b: str) -> str:
    """ Input are two strings a and b consisting only of 1s and 0s.
    Perform binary XOR on these inputs and return result also as a string.
    >>> string_xor('010', '110')
    '100'
    """
    # convert to binary
    a, b = map(lambda x: format(int(x, 2), '08b'), (a, b))
    return ''.join('0' if x == y else '1' for x, y in zip(a, b))

