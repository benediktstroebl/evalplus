from typing import List


def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    """ Insert a number 'delimeter' between every two consecutive elements of input list `numbers'
    >>> intersperse([], 4)
    []
    >>> intersperse([1, 2, 3], 4)
    [1, 4, 2, 4, 3]
    """

    if len(numbers) <= 1:
        return numbers
    else:
        return [numbers[0]] + intersperse(numbers[1:], delimeter)
        # intersperse([1, 2, 3], 4) → [1, 4, 2, 4, 3]
        # intersperse([4, 2, 3], 4) → [4, 2, 4, 3]
        # intersperse([5, 3, 2], 4) → [5, 3, 4, 2]
        # intersperse([5, 2, 1], 4) → [5, 4, 2, 4, 1]
        # intersperse([1, 4, 2, 3], 4) → [1, 4, 2, 4, 3]
        # intersperse([4, 2, 4, 3], 4) → [4, 2, 4, 3]
        # intersperse([5, 3, 4, 2], 4) → [5, 3, 4, 2]
        # intersperse([5, 2, 4, 1], 4) → [5, 2, 4, 1]
