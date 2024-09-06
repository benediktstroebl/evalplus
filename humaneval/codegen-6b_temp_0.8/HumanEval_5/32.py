from typing import List


def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    """ Insert a number 'delimeter' between every two consecutive elements of input list `numbers'
    >>> intersperse([], 4)
    []
    >>> intersperse([1, 2, 3], 4)
    [1, 4, 2, 4, 3]
    """
    result = []
    for i in range(1, len(numbers), 2):
        result.append(numbers[i - 1])
        result.append(delimeter)
        result.append(numbers[i])
    if result[-1] != delimeter:
        result.append(numbers[-1])
    return result

