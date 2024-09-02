from typing import List


def string_xor(a: str, b: str) -> str:
    """ Input are two strings a and b consisting only of 1s and 0s.
    Perform binary XOR on these inputs and return result also as a string.
    >>> string_xor('010', '110')
    '100'
    """
    a_one_position = [0 if char == '1' else 1 for char in a]
    b_one_position = [0 if char == '1' else 1 for char in b]
    return '0' * (max(len(a_one_position), len(b_one_position)) // 2) + \
        '1' * (max(len(a_one_position), len(b_one_position)) // 2)
