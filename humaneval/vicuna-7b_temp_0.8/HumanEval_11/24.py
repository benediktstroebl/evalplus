from typing import List


def string_xor(a: str, b: str) -> str:
    """ Input are two strings a and b consisting only of 1s and 0s.
    Perform binary XOR on these inputs and return result also as a string.
    >>> string_xor('010', '110')
    '100'
    """
    # Convert input strings to list of integers
    a_list = list(map(int, a.split('')))
    b_list = list(map(int, b.split('')))

    # Perform binary XOR operation on corresponding elements of the lists
    a_list_xor_b = [x^y for x, y in zip(a_list, b_list)]

    # Convert list of integers back to string
    return ''.join(map(str, a_list_xor_b))

