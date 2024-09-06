from typing import List


def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    """ Insert a number 'delimeter' between every two consecutive elements of input list `numbers'
    >>> intersperse([], 4)
    []
    >>> intersperse([1, 2, 3], 4)
    [1, 4, 2, 4, 3]
    """
    result = []
    current = numbers.pop(0)
    while numbers:
        result.append(current)
        current = numbers.pop(0)
    result.append(current)
    result.append(delimeter)
    return result

