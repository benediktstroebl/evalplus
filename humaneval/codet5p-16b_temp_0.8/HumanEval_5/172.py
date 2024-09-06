from typing import List


def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    """ Insert a number 'delimeter' between every two consecutive elements of input list `numbers'
    >>> intersperse([], 4)
    []
    >>> intersperse([1, 2, 3], 4)
    [1, 4, 2, 4, 3]
    """

    new_numbers = []
    for i in range(len(numbers) - 1):
        new_numbers.extend([numbers[i], delimeter])
    return new_numbers + [numbers[-1]]
