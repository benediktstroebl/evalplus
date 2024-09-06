from typing import List


def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    """ Insert a number 'delimeter' between every two consecutive elements of input list `numbers'
    >>> intersperse([], 4)
    []
    >>> intersperse([1, 2, 3], 4)
    [1, 4, 2, 4, 3]
    """

    assert len(numbers) >= 1, "No input list provided"
    assert delimeter >= 0, "delimeter value can not be negative"
    return [numbers[0]] + [delimeter] * len(numbers[1:-1]) + [numbers[-1]]
