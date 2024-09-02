from typing import List


def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    """ Insert a number 'delimeter' between every two consecutive elements of input list `numbers'
    >>> intersperse([], 4)
    []
    >>> intersperse([1, 2, 3], 4)
    [1, 4, 2, 4, 3]
    """
    if len(numbers) == 0:
        return numbers

    if len(numbers) == 1:
        return numbers

    result = [numbers[0]]
    for i in range(1, len(numbers)):
        result.append(numbers[i])
        result.append(delimeter)

    return result[:-1
