from typing import List


def string_xor(a: str, b: str) -> str:
    """ Input are two strings a and b consisting only of 1s and 0s.
    Perform binary XOR on these inputs and return result also as a string.
    >>> string_xor('010', '110')
    '100'
    """
    # a = '1100'
    # b = '1011'
    len_a = len(a)
    len_b = len(b)
    result = []
    for i in range(max(len_a, len_b)):
        if i < len_a:
            result.append(str((int(a[i]) + int(b[i])) % 2))
        else:
            result.append(str((int(b[i]) + int(a[i])) % 2))
    return "".join(result)

