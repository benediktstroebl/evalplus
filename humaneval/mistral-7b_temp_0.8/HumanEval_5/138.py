from typing import List


def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    """ Insert a number 'delimeter' between every two consecutive elements of input list `numbers'
    >>> intersperse([], 4)
    []
    >>> intersperse([1, 2, 3], 4)
    [1, 4, 2, 4, 3]
    """
    new_list = []
    i = 0
    while i < len(numbers):
        new_list.append(numbers[i])
        new_list.append(delimeter)
        i += 1
    return new_list

