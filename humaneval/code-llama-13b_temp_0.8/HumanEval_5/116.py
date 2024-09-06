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
        for index, item in enumerate(numbers)
        if index == 0
        or (index % 2 == 1 and index != len(numbers) - 1)
        or index == len(numbers) - 1
    ]

