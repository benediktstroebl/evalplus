from typing import List


def string_xor(a: str, b: str) -> str:
    """ Input are two strings a and b consisting only of 1s and 0s.
    Perform binary XOR on these inputs and return result also as a string.
    >>> string_xor('010', '110')
    '100'
    """
    result = []
    for (bit_a, bit_b) in zip(a, b):
        bit = int(bit_a) ^ int(bit_b)
        result.append(str(bit))
    return "".join(result)

