from typing import List


def string_xor(a: str, b: str) -> str:
    """ Input are two strings a and b consisting only of 1s and 0s.
    Perform binary XOR on these inputs and return result also as a string.
    >>> string_xor('010', '110')
    '100'
    """
    length = min(len(a), len(b))
    result = ''
    for i in range(length):
        xor_value = int(a[i]) ^ int(b[i])
        result += str(xor_value)
    return result

