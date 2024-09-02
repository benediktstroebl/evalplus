from typing import List


def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    """ Insert a number 'delimeter' between every two consecutive elements of input list `numbers'
    >>> intersperse([], 4)
    []
    >>> intersperse([1, 2, 3], 4)
    [1, 4, 2, 4, 3]
    """
    i = 0
    l = len(numbers)
    result = numbers[:]
    while i < l - 1:
        result.insert(i+1, delimeter)
        i += 2
    return result

