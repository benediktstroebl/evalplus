from typing import List


def string_xor(a: str, b: str) -> str:
    """ Input are two strings a and b consisting only of 1s and 0s.
    Perform binary XOR on these inputs and return result also as a string.
    >>> string_xor('010', '110')
    '100'
    """

    def xor(a: str, b: str):
        return '1' if a!= b else '0'

    # check the length of both strings
    assert len(a) == len(b), "Length of both strings should be same"

    return "".join(map(xor, a, b))

