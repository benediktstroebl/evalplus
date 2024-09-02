from typing import List


def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    """ Insert a number 'delimeter' between every two consecutive elements of input list `numbers'
    >>> intersperse([], 4)
    []
    >>> intersperse([1, 2, 3], 4)
    [1, 4, 2, 4, 3]
    """
    new_numbers = []
    for i, number in enumerate(numbers):
        if i > 0:
            new_numbers.append(delimeter)
        new_numbers.append(number)
    return new_n
