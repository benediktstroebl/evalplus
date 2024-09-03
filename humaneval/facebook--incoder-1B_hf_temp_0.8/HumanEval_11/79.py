from typing import List


def string_xor(a: str, b: str) -> str:
    """ Input are two strings a and b consisting only of 1s and 0s.
    Perform binary XOR on these inputs and return result also as a string.
    >>> string_xor('010', '110')
    '100'
    """
    # https://www.codechef.com/problems/XOR
    bits = set(a) | set(b)
    sum_bits = sum(bits)
    bit_pos = sum_bits
    result = ''
    while bit_pos >= 32:
        result = ''.join([result, chr(bit_pos % 16)])
        bit_pos /= 16
    return ''.join(result)

