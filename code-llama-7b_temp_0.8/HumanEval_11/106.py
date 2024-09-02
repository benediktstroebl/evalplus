from typing import List


def string_xor(a: str, b: str) -> str:
    """ Input are two strings a and b consisting only of 1s and 0s.
    Perform binary XOR on these inputs and return result also as a string.
    >>> string_xor('010', '110')
    '100'
    """

    # Convert input strings to lists
    a_list = [int(x) for x in a]
    b_list = [int(x) for x in b]

    # Perform XOR on lists
    c_list = [a_list[i] ^ b_list[i] for i in range(len(a_list))]

    # Convert list to string and return
    return "".join(str(x) for x in c_list)

