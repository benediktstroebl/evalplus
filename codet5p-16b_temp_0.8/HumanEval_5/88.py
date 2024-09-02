from typing import List


def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    """ Insert a number 'delimeter' between every two consecutive elements of input list `numbers'
    >>> intersperse([], 4)
    []
    >>> intersperse([1, 2, 3], 4)
    [1, 4, 2, 4, 3]
    """

    result = [delimeter] * (len(numbers) * 2)
    for i in range(len(numbers)):
        result[2 * i + 1] = numbers[i]
    return result
    
