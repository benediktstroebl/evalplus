from typing import List


def string_xor(a: str, b: str) -> str:
    """ Input are two strings a and b consisting only of 1s and 0s.
    Perform binary XOR on these inputs and return result also as a string.
    >>> string_xor('010', '110')
    '100'
    """
    xor_list = list(bin(a)[2:])
    xor_list.append(bin(b)[2:])
    xor_list.pop(0)
    return "".join(xor_list)

