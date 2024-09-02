from typing import List


def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    """ Insert a number 'delimeter' between every two consecutive elements of input list `numbers'
    >>> intersperse([], 4)
    []
    >>> intersperse([1, 2, 3], 4)
    [1, 4, 2, 4, 3]
    """
    intersperse_result = []
    for number in numbers:
        intersperse_result.append(number)
        intersperse_result.append(delimeter)
    return intersperse_result
