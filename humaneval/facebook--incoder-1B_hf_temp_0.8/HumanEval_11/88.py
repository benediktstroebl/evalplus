from typing import List


def string_xor(a: str, b: str) -> str:
    """ Input are two strings a and b consisting only of 1s and 0s.
    Perform binary XOR on these inputs and return result also as a string.
    >>> string_xor('010', '110')
    '100'
    """
    # https://www.geeksforgeeks.org/binary-string-reversal-or-xor/
    a, b = a[::-1], b[::-1]
    a_len = len(a)
    b_len = len(b)
    result = []
    while a_len and b_len:
        # a[0] and b[0] has same binary representation
        if a[0] == b[0]:
            result.append(a[0])
            a_len -= 1
        else:
            result.append(b[0])
            b_len -= 1
    # binary XOR of remaining bit sequences is 0
    return "".join(result)

