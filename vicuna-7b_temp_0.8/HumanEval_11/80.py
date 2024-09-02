from typing import List


def string_xor(a: str, b: str) -> str:
    """ Input are two strings a and b consisting only of 1s and 0s.
    Perform binary XOR on these inputs and return result also as a string.
    >>> string_xor('010', '110')
    '100'
    """
    # Check if both inputs are empty
    if not a and not b:
        return ''
    # Check if both inputs are empty
    if not a and b:
        return b
    # Check if both inputs are same
    if a == b:
        return ''
    # XOR of two inputs
    xor = 0
    for i in range(max(len(a), len(b))):
        if a[i] == '1':
            xor ^= 1
        elif b[i] == '1':
            xor ^= 1
    return '0' * (len(a) - len(xor)) + str(xor)

