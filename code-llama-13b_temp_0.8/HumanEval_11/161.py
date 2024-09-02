from typing import List


def string_xor(a: str, b: str) -> str:
    """ Input are two strings a and b consisting only of 1s and 0s.
    Perform binary XOR on these inputs and return result also as a string.
    >>> string_xor('010', '110')
    '100'
    """
    # check if input are valid
    if len(a) != len(b):
        raise ValueError("Both input strings need to be of equal length")
    else:
        return ''.join(['1' if int(i) ^ int(j) else '0' for i, j in zip(a, b)])

