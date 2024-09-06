from typing import List


def string_xor(a: str, b: str) -> str:
    """ Input are two strings a and b consisting only of 1s and 0s.
    Perform binary XOR on these inputs and return result also as a string.
    >>> string_xor('010', '110')
    '100'
    """

    # You may want to use list comprehension and map(int, list) to convert
    # a and b into lists of ints (0s and 1s).
    # Your code here
    return "".join([str(a ^ b) for (a, b) in zip(a, b)])

