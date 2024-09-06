from typing import List


def string_xor(a: str, b: str) -> str:
    """ Input are two strings a and b consisting only of 1s and 0s.
    Perform binary XOR on these inputs and return result also as a string.
    >>> string_xor('010', '110')
    '100'
    """
    # First, convert the strings into lists of characters
    a_list = list(a)
    b_list = list(b)
    # Next, perform XOR on those lists
    result = [int(ai) ^ int(bi) for ai, bi in zip(a_list, b_list)]
    # Finally, convert the resulting list into a string
    return "".join([str(i) for i in result])

