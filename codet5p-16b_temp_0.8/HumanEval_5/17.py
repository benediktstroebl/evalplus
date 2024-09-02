from typing import List


def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    """ Insert a number 'delimeter' between every two consecutive elements of input list `numbers'
    >>> intersperse([], 4)
    []
    >>> intersperse([1, 2, 3], 4)
    [1, 4, 2, 4, 3]
    """

    assert len(numbers) >= 2
    if len(numbers) == 2:
        return [numbers[0], delimeter, numbers[1]]
    return [numbers[0]] + intersperse(numbers[1:-1], delimeter) + [numbers[-1]]
