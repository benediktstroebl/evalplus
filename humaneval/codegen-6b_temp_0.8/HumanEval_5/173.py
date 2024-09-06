from typing import List


def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    """ Insert a number 'delimeter' between every two consecutive elements of input list `numbers'
    >>> intersperse([], 4)
    []
    >>> intersperse([1, 2, 3], 4)
    [1, 4, 2, 4, 3]
    """
    new_list = []
    for i in range(0, len(numbers), 2):
        new_list.append(numbers[i])
        new_list.append(delimeter)
        if i + 1 < len(numbers):
            new_list.append(numbers[i + 1])
    return new_list

