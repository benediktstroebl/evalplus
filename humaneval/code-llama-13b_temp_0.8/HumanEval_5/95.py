from typing import List


def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    """ Insert a number 'delimeter' between every two consecutive elements of input list `numbers'
    >>> intersperse([], 4)
    []
    >>> intersperse([1, 2, 3], 4)
    [1, 4, 2, 4, 3]
    """

    numbers_copy = numbers.copy()
    for i in range(0, len(numbers_copy) - 1):
        numbers_copy.insert(i * 2 + 1, delimeter)
    return numbers_copy

