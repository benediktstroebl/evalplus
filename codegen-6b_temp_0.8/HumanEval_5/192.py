from typing import List


def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    """ Insert a number 'delimeter' between every two consecutive elements of input list `numbers'
    >>> intersperse([], 4)
    []
    >>> intersperse([1, 2, 3], 4)
    [1, 4, 2, 4, 3]
    """
    assert numbers, "Cannot process empty list."
    assert delimeter > 0, "Delimiter should be positive."
    n = len(numbers)
    return [delimeter] * (n % 2) + numbers + [delimeter] * (n % 2)

