from typing import List


def string_xor(a: str, b: str) -> str:
    """ Input are two strings a and b consisting only of 1s and 0s.
    Perform binary XOR on these inputs and return result also as a string.
    >>> string_xor('010', '110')
    '100'
    """
    def xor_bit(i, a_bit, b_bit):
        if a_bit == b_bit:
            return "0"
        elif a_bit == "1" and b_bit == "0":
            return "1"
        else:
            return "0"

    string_length = len(a) + len(b)
    result = "0" * string_length
    for i in range(string_length):
        result[i] = xor_bit(i, a[i], b[i])
    return result

