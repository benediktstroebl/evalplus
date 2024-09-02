from typing import List


def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    """ Insert a number 'delimeter' between every two consecutive elements of input list `numbers'
    >>> intersperse([], 4)
    []
    >>> intersperse([1, 2, 3], 4)
    [1, 4, 2, 4, 3]
    """
    n = len(numbers)
    if n == 0:
        return numbers
    else:
        return numbers[0:n // 2] + [delimeter] + numbers[n // 2:n]
