from typing import List


def string_xor(a: str, b: str) -> str:
    """ Input are two strings a and b consisting only of 1s and 0s.
    Perform binary XOR on these inputs and return result also as a string.
    >>> string_xor('010', '110')
    '100'
    """
    # initialize result to "" (empty string)
    result = ""
    # loop over all pairs of bits from a and b
    for i in range(len(a)):
        for j in range(i+1, len(a)):
            # if both bits are 1 or both bits are 0, do nothing
            if (a[i] == '1' and b[j] == '1') or (a[i] == '0' and b[j] == '0'):
                continue
            # else XOR the bits and update the result
            result += str(int(a[i]) ^ int(b[j]))
    return result

