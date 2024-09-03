from typing import List


def string_xor(a: str, b: str) -> str:
    """ Input are two strings a and b consisting only of 1s and 0s.
    Perform binary XOR on these inputs and return result also as a string.
    >>> string_xor('010', '110')
    '100'
    """
    if a == b:
        return a
    a_len = len(a)
    b_len = len(b)
    assert a_len == b_len
    if a_len == 1 and b_len == 1:
        return int(a[0]^b[0], 2)
    return ''.join(map(lambda x: str(int(x^b[0], 2)), itertools.chain(*[a[::2]]*2)))

