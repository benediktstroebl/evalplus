from typing import List


def string_xor(a: str, b: str) -> str:
    """ Input are two strings a and b consisting only of 1s and 0s.
    Perform binary XOR on these inputs and return result also as a string.
    >>> string_xor('010', '110')
    '100'
    """
    return ''.join(map(lambda a, b: '1' if (a == '1' and b == '0') or (a == '0' and b == '1') else '0', a, b))

