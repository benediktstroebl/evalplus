from typing import List


def string_xor(a: str, b: str) -> str:
    """ Input are two strings a and b consisting only of 1s and 0s.
    Perform binary XOR on these inputs and return result also as a string.
    >>> string_xor('010', '110')
    '100'
    """
    if len(a)!= len(b):
        raise ValueError("Length of inputs to string_xor should be equal")

    output = ""
    for a_bit, b_bit in zip(a, b):
        output += str(int(a_bit) ^ int(b_bit))

    return output

