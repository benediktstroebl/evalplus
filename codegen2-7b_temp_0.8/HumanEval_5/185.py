from typing import List


def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    """ Insert a number 'delimeter' between every two consecutive elements of input list `numbers'
    >>> intersperse([], 4)
    []
    >>> intersperse([1, 2, 3], 4)
    [1, 4, 2, 4, 3]
    """
    if not isinstance(numbers, list):
        raise TypeError(f"{numbers} must be a list!")
    if not isinstance(delimeter, int):
        raise TypeError(f"{delimeter} must be an int!")

    return [numbers[0]] + [delimeter] + [n for n in numbers[1:] if n!= delimeter] + [delimeter
