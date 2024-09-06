from typing import List


def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    """ Insert a number 'delimeter' between every two consecutive elements of input list `numbers'
    >>> intersperse([], 4)
    []
    >>> intersperse([1, 2, 3], 4)
    [1, 4, 2, 4, 3]
    """

    result = []
    for num in numbers:
        result.append(num)
        if len(numbers) > 1 and result[-1] != numbers[-1]:
            result.append(delimeter)

    return result
