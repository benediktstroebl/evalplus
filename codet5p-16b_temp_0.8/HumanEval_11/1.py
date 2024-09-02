from typing import List


def string_xor(a: str, b: str) -> str:
    """ Input are two strings a and b consisting only of 1s and 0s.
    Perform binary XOR on these inputs and return result also as a string.
    >>> string_xor('010', '110')
    '100'
    """

    a_bits = list(a)
    b_bits = list(b)

    return ''.join(
        [
            '1' if (bits[0] == '1' and bits[1] == '0') or (bits[0] == '0' and bits[1] == '1') else '0'
            for bits in zip(a_bits, b_bits)
        ]
    )

