from typing import List


def string_xor(a: str, b: str) -> str:
    """ Input are two strings a and b consisting only of 1s and 0s.
    Perform binary XOR on these inputs and return result also as a string.
    >>> string_xor('010', '110')
    '100'
    """
    # check if inputs are non-empty strings
    if len(a) == 0 or len(b) == 0:
        return '0'

    # convert each input to list of 1s and 0s
    a_list = List(a)
    b_list = List(b)

    # perform binary XOR on the lists
    result_list = [x ^ y for x, y in zip(a_list, b_list)]

    # convert the list of 1s and 0s back to a string
    result = ''.join(str(x) for x in result_list)

    return result

