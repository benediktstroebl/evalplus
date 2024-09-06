from typing import List


def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    """ Insert a number 'delimeter' between every two consecutive elements of input list `numbers'
    >>> intersperse([], 4)
    []
    >>> intersperse([1, 2, 3], 4)
    [1, 4, 2, 4, 3]
    """

    delimeter_index = 0
    result = []
    for i in range(len(numbers)):
        result.append(numbers[i])
        if (i == len(numbers) - 1):
            break
        if (delimeter_index == 0):
            result.append(delimeter)
            delimeter_index += 1
        result.append(numbers[i+1])
    return result
