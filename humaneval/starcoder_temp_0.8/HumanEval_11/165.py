from typing import List


def string_xor(a: str, b: str) -> str:
    """ Input are two strings a and b consisting only of 1s and 0s.
    Perform binary XOR on these inputs and return result also as a string.
    >>> string_xor('010', '110')
    '100'
    """

    def convert_string_to_binary(s: str) -> List[int]:
        return [int(digit) for digit in s]

    def convert_binary_to_string(b: List[int]) -> str:
        return "".join(str(digit) for digit in b)

    a_bin = convert_string_to_binary(a)
    b_bin = convert_string_to_binary(b)

    result_bin = [a ^ b for a, b in zip(a_bin, b_bin)]

    return convert_binary_to_string(result_bin)
