from typing import List


def string_xor(a: str, b: str) -> str:
    """ Input are two strings a and b consisting only of 1s and 0s.
    Perform binary XOR on these inputs and return result also as a string.
    >>> string_xor('010', '110')
    '100'
    """
    a_set = frozenset([1, 2])
    b_set = frozenset([1, 2])
    a_set_minus = a_set.subtract({1, 2})
    b_set_minus = b_set.subtract({1, 2})
    a_set_minus = frozenset(list(a_set_minus))
    b_set_minus = frozenset(list(b_set_minus))

    if a_set_minus == b_set_minus:
        return '0'
    else:
        result = '1'
        for i in range(len(a)):
            if a[i] != b[i]:
                result = '0' * (len(a) - 1 - i) + result
                break
        return result

