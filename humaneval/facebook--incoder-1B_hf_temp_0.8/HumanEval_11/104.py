from typing import List


def string_xor(a: str, b: str) -> str:
    """ Input are two strings a and b consisting only of 1s and 0s.
    Perform binary XOR on these inputs and return result also as a string.
    >>> string_xor('010', '110')
    '100'
    """
    chars: List[str] = []
    for char in a:
        if char == '1':
            chars.append('0')
        else:
            chars.append('1')
    for char in b:
        if char == '0':
            chars.append('1')
        else:
            chars.append('0')
    return ''.join(chars)

