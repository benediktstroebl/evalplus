from typing import List


def string_xor(a: str, b: str) -> str:
    """ Input are two strings a and b consisting only of 1s and 0s.
    Perform binary XOR on these inputs and return result also as a string.
    >>> string_xor('010', '110')
    '100'
    """
    # Get the lengths of a and b
    na = len(a)
    nb = len(b)

    # Initialize an empty string to store the result
    res = ''

    # Loop over all the characters of a and b
    for i in range(na):
        # If the current character of a is 0, set the corresponding
        # position in the result to 0
        if a[i] == '0':
            res += '0'
        # If the current character of b is 0, set the corresponding
        # position in the result to 1
        elif b[i] == '0':
            res += '1'
        # If the current characters are different, the result is 1
        # at the corresponding positions
        else:
            res += '1'

    return res
