from typing import List


def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    """ Insert a number 'delimeter' between every two consecutive elements of input list `numbers'
    >>> intersperse([], 4)
    []
    >>> intersperse([1, 2, 3], 4)
    [1, 4, 2, 4, 3]
    """
    result = []

    if len(numbers) == 0:
        return result

    for i, value in enumerate(numbers):
        if i == len(numbers) - 1:
            result.append(value)
        else:
            result.append(value)
            result.append(delimeter)

    return result

