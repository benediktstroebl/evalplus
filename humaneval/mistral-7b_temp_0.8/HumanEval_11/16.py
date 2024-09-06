from typing import List


def string_xor(a: str, b: str) -> str:
    """ Input are two strings a and b consisting only of 1s and 0s.
    Perform binary XOR on these inputs and return result also as a string.
    >>> string_xor('010', '110')
    '100'
    """

    a_bin = list(a)
    b_bin = list(b)
    n = len(a_bin)
    result = ""
    for i in range(n):
        a_bit = int(a_bin[i])
        b_bit = int(b_bin[i])
        xor_bit = a_bit ^ b_bit
        result += str(xor_bit)

    return result

