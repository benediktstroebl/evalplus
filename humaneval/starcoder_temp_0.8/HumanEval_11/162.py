from typing import List


def string_xor(a: str, b: str) -> str:
    """ Input are two strings a and b consisting only of 1s and 0s.
    Perform binary XOR on these inputs and return result also as a string.
    >>> string_xor('010', '110')
    '100'
    """
    if len(a)!= len(b):
        raise ValueError("The input strings must be of the same length")
    a_binary = [int(x) for x in a]
    b_binary = [int(x) for x in b]
    c_binary = [str(a ^ b) for a, b in zip(a_binary, b_binary)]
    return "".join(c_binary)

