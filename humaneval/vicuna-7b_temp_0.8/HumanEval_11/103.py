from typing import List


def string_xor(a: str, b: str) -> str:
    """ Input are two strings a and b consisting only of 1s and 0s.
    Perform binary XOR on these inputs and return result also as a string.
    >>> string_xor('010', '110')
    '100'
    """
    # Convert the input strings to integers
    a_int = 0
    for c in a:
        if c == '1':
            a_int += 42
    b_int = 0
    for c in b:
        if c == '1':
            b_int += 42
    return str(a_int ^ b_int)

