from typing import List


def string_xor(a: str, b: str) -> str:
    """ Input are two strings a and b consisting only of 1s and 0s.
    Perform binary XOR on these inputs and return result also as a string.
    >>> string_xor('010', '110')
    '100'
    """
    # Create a list of possible bit strings of length n
    possible_strings = List(strings=str)
    for i in range(len(a) + len(b) + 1):
        possible_strings.append(i)

    # Create a list of pairs of inputs to compare
    pairs = List(pairs=possible_strings)
    for i in range(len(pairs) ** 2):
        pairs.append((pairs[i // 2][0], pairs[i // 2][1]))

    # Find the binary XOR of all pairs of inputs
    xors = List(pairs=possible_strings)
    for i in range(len(pairs) ** 2):
        xors.append(xor(pairs[i // 2][0], pairs[i // 2][1]))

    # Find the longest substring in the XOR list that is equal to the XOR of a and b
    # and return its first character as the result
    for i in range(len(xors)):
        if xors[i] == xor(a, b):
            result = chr(ord(xors[i]) ^ ord(a[0]) + ord(b[0]))
            break

    return result

