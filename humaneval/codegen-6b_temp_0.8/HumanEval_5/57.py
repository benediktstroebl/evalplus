from typing import List


def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    """ Insert a number 'delimeter' between every two consecutive elements of input list `numbers'
    >>> intersperse([], 4)
    []
    >>> intersperse([1, 2, 3], 4)
    [1, 4, 2, 4, 3]
    """
    new = []
    for index, number in enumerate(numbers[: - 1], 1):
        if index % 2 == 0:
            new.append(number)
        new.append(delimeter)
        new.append(number)
    new.append(numbers[-1])
    return new

