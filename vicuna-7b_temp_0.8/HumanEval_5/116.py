from typing import List


def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    """ Insert a number 'delimeter' between every two consecutive elements of input list `numbers'
    >>> intersperse([], 4)
    []
    >>> intersperse([1, 2, 3], 4)
    [1, 4, 2, 4, 3]
    """
    length = len(numbers)
    result = [numbers[i:i+1] for i in range(length)]
    for i in range(length // 2):
        result[i:i+1].insert(0, delimeter)
    return result

