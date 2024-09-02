from typing import List


def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    """ Insert a number 'delimeter' between every two consecutive elements of input list `numbers'
    >>> intersperse([], 4)
    []
    >>> intersperse([1, 2, 3], 4)
    [1, 4, 2, 4, 3]
    """
    if len(numbers) < 2:
        return numbers

    # out: the output list
    out: List[int] = []
    for i, n in enumerate(numbers):
        # We skip the first and the last element of the list
        if i > 0 and i < len(numbers) - 1:
            out.append(delimeter)
        out.append(n)
    return out

