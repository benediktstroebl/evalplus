from typing import List


def string_xor(a: str, b: str) -> str:
    """ Input are two strings a and b consisting only of 1s and 0s.
    Perform binary XOR on these inputs and return result also as a string.
    >>> string_xor('010', '110')
    '100'
    """
    def xor(input1: str, input2: str) -> str:
        result = ""
        for i in range(len(input1)):
            if input1[i] == input2[i]:
                result += '0'
            else:
                result += '1'
        return result

    return xor(a, b)

