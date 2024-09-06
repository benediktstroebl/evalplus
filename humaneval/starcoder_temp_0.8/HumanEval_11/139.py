from typing import List


def string_xor(a: str, b: str) -> str:
    """ Input are two strings a and b consisting only of 1s and 0s.
    Perform binary XOR on these inputs and return result also as a string.
    >>> string_xor('010', '110')
    '100'
    """

    # convert the strings a and b to their binary representations
    # and then convert them to list of ints
    a = [int(x) for x in list(bin(int(a, 2))[2:])]
    b = [int(x) for x in list(bin(int(b, 2))[2:])]

    # pad the lists a and b with zeros so that they are of equal length
    if len(a) > len(b):
        b = [0 for x in range(len(a) - len(b))] + b
    elif len(a) < len(b):
        a = [0 for x in range(len(b) - len(a))] + a

    # perform XOR operation on each pair of bits
    result = [str(x ^ y) for x, y in zip(a, b)]
    result = ''.join(result)

    return result

