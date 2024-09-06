from typing import List


def string_xor(a: str, b: str) -> str:
    """ Input are two strings a and b consisting only of 1s and 0s.
    Perform binary XOR on these inputs and return result also as a string.
    >>> string_xor('010', '110')
    '100'
    """
    # convert each input to binary and pad it with 0s to make
    # the length equal to the max of a and b.
    # Use format specifier to pad with 0s in front.
    a_bin = "{:0{}b}".format(int(a, 2), max(len(a), len(b)))
    b_bin = "{:0{}b}".format(int(b, 2), max(len(a), len(b)))
    # use list comprehension to iterate over the binary strings
    # convert to int and perform XOR operation.
    result = [str(int(x, 2) ^ int(y, 2)) for x, y in zip(a_bin, b_bin)]
    # convert the result list to a string and return it.
    return "".join(result)

