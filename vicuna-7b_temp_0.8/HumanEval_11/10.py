from typing import List


def string_xor(a: str, b: str) -> str:
    """ Input are two strings a and b consisting only of 1s and 0s.
    Perform binary XOR on these inputs and return result also as a string.
    >>> string_xor('010', '110')
    '100'
    """
    a_set = {0, 1}
    b_set = {0, 1}
    result_set = {0, 1}

    for char_a in a:
        if char_a in a_set:
            result_set.remove(char_a)
        else:
            result_set.add(char_a)

    for char_b in b:
        if char_b in b_set:
            result_set.remove(char_b)
        else:
            result_set.add(char_b)

    return ''.join(result_set)
