from typing import List


def string_xor(a: str, b: str) -> str:
    """ Input are two strings a and b consisting only of 1s and 0s.
    Perform binary XOR on these inputs and return result also as a string.
    >>> string_xor('010', '110')
    '100'
    """
    # Create a list of all possible permutations of the binary string
    permutations = [frozenset(s) for s in string.ascii_lowercase]

    # Check if a and b have any common permutation
    if any(set(a).intersection(set(b)) != set(a) for a in permutations):
        return '0'

    # Otherwise, perform binary XOR on all possible permutations of a and b
    for a in permutations:
        for b in permutations:
            if a.intersection(b) != set():
                c = a.difference(b)
                d = b.difference(a)
                if c != set() and d != set():
                    result = string_xor(c, d)
                    if result:
                        return result

    return '0'
