from typing import List


def string_xor(a: str, b: str) -> str:
    """ Input are two strings a and b consisting only of 1s and 0s.
    Perform binary XOR on these inputs and return result also as a string.
    >>> string_xor('010', '110')
    '100'
    """
    # Add your code here
    a_list = list(a)
    b_list = list(b)
    result = [chr(int(a_list[i]) ^ int(b_list[i])) for i in range(len(a_list))]
    return ''.join(result)

