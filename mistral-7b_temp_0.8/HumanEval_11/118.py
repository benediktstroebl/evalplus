from typing import List


def string_xor(a: str, b: str) -> str:
    """ Input are two strings a and b consisting only of 1s and 0s.
    Perform binary XOR on these inputs and return result also as a string.
    >>> string_xor('010', '110')
    '100'
    """

    def bit_xor(a, b):
        """
        Perform bitwise XOR on two bits and return the result.
        >>> bit_xor(0, 0)
        0
        >>> bit_xor(0, 1)
        1
        >>> bit_xor(1, 0)
        1
        >>> bit_xor(1, 1)
        0
        """
        return int(str(int(a) ^ int(b)), 2)

    res = ""
    for i in range(len(a)):
        res += str(bit_xor(a[i], b[i]))
    return res

