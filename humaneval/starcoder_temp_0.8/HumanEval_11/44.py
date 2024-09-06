from typing import List


def string_xor(a: str, b: str) -> str:
    """ Input are two strings a and b consisting only of 1s and 0s.
    Perform binary XOR on these inputs and return result also as a string.
    >>> string_xor('010', '110')
    '100'
    """
    if len(a)!= len(b):
        raise ValueError('Inputs must be of same length')

    binary_xor_result: List[str] = []

    for bit_a, bit_b in zip(a, b):
        binary_xor_result.append(str(int(bit_a) ^ int(bit_b)))

    return ''.join(binary_xor_result)

