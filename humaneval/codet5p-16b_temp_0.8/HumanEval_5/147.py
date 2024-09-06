from typing import List


def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    """ Insert a number 'delimeter' between every two consecutive elements of input list `numbers'
    >>> intersperse([], 4)
    []
    >>> intersperse([1, 2, 3], 4)
    [1, 4, 2, 4, 3]
    """

    out = []
    for i in range(len(numbers) - 1):
        out += numbers[i : i + 2]
        out.append(delimeter)
    out += numbers[len(numbers) - 1 : ]
    return out

