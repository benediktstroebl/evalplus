from typing import List


def string_xor(a: str, b: str) -> str:
    """ Input are two strings a and b consisting only of 1s and 0s.
    Perform binary XOR on these inputs and return result also as a string.
    >>> string_xor('010', '110')
    '100'
    """
    if len(a)!= len(b):
        raise ValueError("The lengths of the strings are not equal")
    else:
        new_string = ""
        for i in range(len(a)):
            if a[i] == "1" and b[i] == "0" or a[i] == "0" and b[i] == "1":
                new_string += "1"
            elif a[i] == "1" and b[i] == "1" or a[i] == "0" and b[i] == "0":
                new_string += "0"
            else:
                raise ValueError("The strings contains characters other than 0 or 1")
        return new_string

