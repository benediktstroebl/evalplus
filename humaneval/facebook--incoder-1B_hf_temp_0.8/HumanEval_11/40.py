from typing import List


def string_xor(a: str, b: str) -> str:
    """ Input are two strings a and b consisting only of 1s and 0s.
    Perform binary XOR on these inputs and return result also as a string.
    >>> string_xor('010', '110')
    '100'
    """
    result = ''
    left = 0
    right = len(b)
    while left < right:
        # set current bit of a
        a >>= 1
        # perform binary XOR on left and right
        result += a[left] ^ b[right]
        left += 1
        right -= 1
    return result

