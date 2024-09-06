from typing import List


def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    """ Insert a number 'delimeter' between every two consecutive elements of input list `numbers'
    >>> intersperse([], 4)
    []
    >>> intersperse([1, 2, 3], 4)
    [1, 4, 2, 4, 3]
    """
    result = []
    for i in range(0, len(numbers) + 1, 2):
        if i < len(numbers):
            result.append(numbers[i])
            result.append(delimeter)
        else:
            # i == len(numbers)
            # we only append the last delimeter, since we do not want to terminate the result list
            # with delimeter at the end
            result.append(numbers[i - 1])
    return result

