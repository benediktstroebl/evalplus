from typing import List


def string_xor(a: str, b: str) -> str:
    """ Input are two strings a and b consisting only of 1s and 0s.
    Perform binary XOR on these inputs and return result also as a string.
    >>> string_xor('010', '110')
    '100'
    """
    # initialize an empty string
    result = ""
    # XOR is commutative, so manually iterate through each character
    for i in range(len(a)):
        # XOR is commutative, so the outcome is 0 or 1
        result += str(int(a[i]) ^ int(b[i]))
    return result

