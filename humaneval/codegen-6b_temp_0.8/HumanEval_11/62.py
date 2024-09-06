from typing import List


def string_xor(a: str, b: str) -> str:
    """ Input are two strings a and b consisting only of 1s and 0s.
    Perform binary XOR on these inputs and return result also as a string.
    >>> string_xor('010', '110')
    '100'
    """
    first_bin, second_bin = map(bin, (a, b))
    first_bin = first_bin[2:]
    second_bin = second_bin[2:]

    if len(first_bin) > len(second_bin):
        second_bin = '0' * (len(first_bin) - len(second_bin)) + second_bin

    elif len(second_bin) > len(first_bin):
        first_bin = '0' * (len(second_bin) - len(first_bin)) + first_bin

    output = ''
    for i in range(len(first_bin)):
        if first_bin[i] == second_bin[i]:
            output += '0'
            continue
        output += '1'

    return output

