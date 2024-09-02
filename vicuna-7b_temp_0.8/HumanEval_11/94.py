from typing import List


def string_xor(a: str, b: str) -> str:
    """ Input are two strings a and b consisting only of 1s and 0s.
    Perform binary XOR on these inputs and return result also as a string.
    >>> string_xor('010', '110')
    '100'
    """
    n = max(len(a), len(b))
    result = ''
    for i in range(n):
        a_digit = a[i]
        b_digit = b[i]
        if a_digit == b_digit:
            result += a_digit
        else:
            result += str(int(a_digit) ^ int(b_digit))
    return result

