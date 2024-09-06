from typing import List


def string_xor(a: str, b: str) -> str:
    """ Input are two strings a and b consisting only of 1s and 0s.
    Perform binary XOR on these inputs and return result also as a string.
    >>> string_xor('010', '110')
    '100'
    """

    if len(a)!= len(b):
        raise ValueError("Inputs to xor must have the same length")

    # convert the strings to lists of ints
    A = [int(i) for i in a]
    B = [int(i) for i in b]

    # perform xor operation
    C = [(x + y) % 2 for x, y in zip(A, B)]

    # convert result list to string
    C = "".join(map(str, C))

    return C

