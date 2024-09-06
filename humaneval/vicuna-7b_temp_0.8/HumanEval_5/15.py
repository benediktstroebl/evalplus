from typing import List


def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    """ Insert a number 'delimeter' between every two consecutive elements of input list `numbers'
    >>> intersperse([], 4)
    []
    >>> intersperse([1, 2, 3], 4)
    [1, 4, 2, 4, 3]
    """
    length = len(numbers)
    result = []
    for i in range(length):
        result.append(numbers[i])
        if i < length - 1:
            result.append(delimeter)
        else:
            result.append(numbers[i + 1])
    return result

