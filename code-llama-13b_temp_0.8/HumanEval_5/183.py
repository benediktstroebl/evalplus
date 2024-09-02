from typing import List


def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    """ Insert a number 'delimeter' between every two consecutive elements of input list `numbers'
    >>> intersperse([], 4)
    []
    >>> intersperse([1, 2, 3], 4)
    [1, 4, 2, 4, 3]
    """

    return [
        value
        for index, value in enumerate(numbers)
        for _ in (range(2) if index != len(numbers) - 1 else range(1))
    ]

