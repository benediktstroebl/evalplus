from typing import List


def string_xor(a: str, b: str) -> str:
    """ Input are two strings a and b consisting only of 1s and 0s.
    Perform binary XOR on these inputs and return result also as a string.
    >>> string_xor('010', '110')
    '100'
    """
    a_char = a.lower()
    b_char = b.lower()
    a_char = [char for char in a_char if not char.isdigit()]
    b_char = [char for char in b_char if not char.isdigit()]
    a_char.sort()
    b_char.sort()
    result = ''.join(map(operator.xor, a_char, b_char))
    result = result[::-1]
    return result

