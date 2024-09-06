from typing import List


def string_xor(a: str, b: str) -> str:
    """ Input are two strings a and b consisting only of 1s and 0s.
    Perform binary XOR on these inputs and return result also as a string.
    >>> string_xor('010', '110')
    '100'
    """

    # if len(a)!= len(b):
    #     raise ValueError("Length of strings must be the same.")

    # a = a.zfill(len(b))
    # b = b.zfill(len(a))
    #
    # return "".join(str(int(x) ^ int(y)) for x, y in zip(a, b))

    if len(a)!= len(b):
        raise ValueError("Length of strings must be the same.")

    # convert strings to integer, then xor, then convert to string
    return "{0:b}".format(int(a, 2) ^ int(b, 2))

