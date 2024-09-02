from typing import List


def string_xor(a: str, b: str) -> str:
    """ Input are two strings a and b consisting only of 1s and 0s.
    Perform binary XOR on these inputs and return result also as a string.
    >>> string_xor('010', '110')
    '100'
    """
    a_indices = [i for i, b in enumerate(a) if b == '1']
    b_indices = [i for i, b in enumerate(b) if b == '1']
    return ''.join(a_indices[i:i+1] for i in b_indices)

