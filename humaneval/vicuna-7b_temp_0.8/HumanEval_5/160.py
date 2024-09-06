from typing import List


def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    """ Insert a number 'delimeter' between every two consecutive elements of input list `numbers'
    >>> intersperse([], 4)
    []
    >>> intersperse([1, 2, 3], 4)
    [1, 4, 2, 4, 3]
    """
    length = len(numbers)
    return [numbers[i] for i in range(0, length, 2) for _ in range(2 * (length // 2))] + [delimeter] * (length - (length // 2))