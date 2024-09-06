from typing import List


def string_xor(a: str, b: str) -> str:
    """ Input are two strings a and b consisting only of 1s and 0s.
    Perform binary XOR on these inputs and return result also as a string.
    >>> string_xor('010', '110')
    '100'
    """
    a_bits = [int(bit) for bit in a]
    b_bits = [int(bit) for bit in b]
    a_xor_b = [a_bits[i] ^ b_bits[i] for i in range(len(a_bits))]
    return ''.join(str(x) for x in a_xor_b)

