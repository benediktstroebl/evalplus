from typing import List


def string_xor(a: str, b: str) -> str:
    """ Input are two strings a and b consisting only of 1s and 0s.
    Perform binary XOR on these inputs and return result also as a string.
    >>> string_xor('010', '110')
    '100'
    """
    chars = [x for x in (a, b) if x in '01']
    if len(chars) == 1:
        return chars[0]
    return ''.join(chars)

