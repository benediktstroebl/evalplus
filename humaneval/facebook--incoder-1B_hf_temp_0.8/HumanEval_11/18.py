from typing import List


def string_xor(a: str, b: str) -> str:
    """ Input are two strings a and b consisting only of 1s and 0s.
    Perform binary XOR on these inputs and return result also as a string.
    >>> string_xor('010', '110')
    '100'
    """
    # convert binary string to ascii string
    a = str(a).encode('ascii')
    b = str(b).encode('ascii')

    # perform XOR on the string
    result = ''
    for i in range(len(a)):
        if a[i] == b[i]:
            result += a[i]
        else:
            result += '1'
    return result

