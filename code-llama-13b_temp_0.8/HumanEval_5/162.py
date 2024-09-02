from typing import List


def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    """ Insert a number 'delimeter' between every two consecutive elements of input list `numbers'
    >>> intersperse([], 4)
    []
    >>> intersperse([1, 2, 3], 4)
    [1, 4, 2, 4, 3]
    """

    new_list = []
    length = len(numbers)
    if length == 0:
        return new_list
    elif length == 1:
        new_list.append(numbers[0])
        return new_list

    new_list.append(numbers[0])
    for i in range(1, length):
        new_list.append(delimeter)
        new_list.append(numbers[i])

    return new_list

