from typing import List


def string_xor(a: str, b: str) -> str:
    """ Input are two strings a and b consisting only of 1s and 0s.
    Perform binary XOR on these inputs and return result also as a string.
    >>> string_xor('010', '110')
    '100'
    """
    a_chars = a.split('')
    b_chars = b.split('')

    result_chars = [x + y for x, y in zip(a_chars, b_chars)]

    result = ''.join(result_chars)
    if len(result) % 2 == 0:
        return '0' + result
    else:
        return '1' + result

