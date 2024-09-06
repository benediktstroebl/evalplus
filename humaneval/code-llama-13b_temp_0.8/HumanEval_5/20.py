from typing import List


def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    """ Insert a number 'delimeter' between every two consecutive elements of input list `numbers'
    >>> intersperse([], 4)
    []
    >>> intersperse([1, 2, 3], 4)
    [1, 4, 2, 4, 3]
    """

    result = []
    index = 0

    while index < len(numbers) - 1:
        result.append(numbers[index])
        result.append(delimeter)
        index += 1

    result.append(numbers[index])

    return result

