from typing import List


def string_xor(a: str, b: str) -> str:
    """ Input are two strings a and b consisting only of 1s and 0s.
    Perform binary XOR on these inputs and return result also as a string.
    >>> string_xor('010', '110')
    '100'
    """
    # Convert inputs to lists of 1s and 0s
    a_list = [int(i) for i in a]
    b_list = [int(j) for j in b]

    # Add corresponding elements and take XOR
    a_list_xor_b_list = [a_list[i] ^ b_list[i] for i in range(len(a_list))]

    # Convert back to string
    result_list = [str(x) for x in a_list_xor_b_list]
    result = ''.join(result_list)

    return result

