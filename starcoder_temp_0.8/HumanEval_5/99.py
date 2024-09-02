from typing import List


def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    """ Insert a number 'delimeter' between every two consecutive elements of input list `numbers'
    >>> intersperse([], 4)
    []
    >>> intersperse([1, 2, 3], 4)
    [1, 4, 2, 4, 3]
    """
    return [
        item
        for index, item in enumerate(numbers[:-1])
        if index % 2 == 0
        for _ in [delimeter]
        for item in [item, delimeter]
    ] + [numbers[-1]]
