from typing import List


def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    """ Insert a number 'delimeter' between every two consecutive elements of input list `numbers'
    >>> intersperse([], 4)
    []
    >>> intersperse([1, 2, 3], 4)
    [1, 4, 2, 4, 3]
    """
    res = []
    for idx in range(1, len(numbers)):
        res.append(numbers[idx - 1])
        res.append(delimeter)
        res.append(numbers[idx])
    return res + [numbers[-1]]

