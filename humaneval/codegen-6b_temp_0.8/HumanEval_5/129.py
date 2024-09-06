from typing import List


def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    """ Insert a number 'delimeter' between every two consecutive elements of input list `numbers'
    >>> intersperse([], 4)
    []
    >>> intersperse([1, 2, 3], 4)
    [1, 4, 2, 4, 3]
    """
    if not numbers:
        return []

    result = [numbers[0]]
    for ind in range(1, len(numbers)):
        if numbers[ind - 1] != delimeter:
            result.append(numbers[ind])
        else:
            result.append(delimeter)
            result.append(numbers[ind])

    return result

