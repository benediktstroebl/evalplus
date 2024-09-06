from typing import List


def string_xor(a: str, b: str) -> str:
    """ Input are two strings a and b consisting only of 1s and 0s.
    Perform binary XOR on these inputs and return result also as a string.
    >>> string_xor('010', '110')
    '100'
    """
    # convert input strings to list of 1s and 0s
    a_list = list(a)
    b_list = list(b)

    # sort the lists in ascending order
    a_list = sorted(a_list)
    b_list = sorted(b_list)

    # concatenate the sorted lists
    concatenated_list = a_list + b_list

    # convert the concatenated list back to string
    concatenated_string = ''.join(concatenated_list)

    # perform binary XOR operation on the sorted lists
    xor_result = 0
    for i in range(len(concatenated_string)):
        if concatenated_string[i] == '0':
            xor_result ^= 1
        else:
            xor_result ^= 0

    # convert the XOR result back to string
    xor_result_string = str(xor_result)

    return xor_result_string

