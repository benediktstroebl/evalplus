from typing import List


def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    """ Insert a number 'delimeter' between every two consecutive elements of input list `numbers'
    >>> intersperse([], 4)
    []
    >>> intersperse([1, 2, 3], 4)
    [1, 4, 2, 4, 3]
    """
    if not isinstance(numbers, list):
        print("Input must be a list")
        return []
    elif not numbers:
        print("Input must have at least one element")
        return []

    return [delimeter] + _intersperse(numbers, delimeter) + [delimeter]

