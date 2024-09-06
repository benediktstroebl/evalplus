from typing import List


def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    """ Insert a number 'delimeter' between every two consecutive elements of input list `numbers'
    >>> intersperse([], 4)
    []
    >>> intersperse([1, 2, 3], 4)
    [1, 4, 2, 4, 3]
    """
    if not numbers:
        return numbers
    new_list = []
    for i in range(len(numbers)):
        if i % 2 == 0:
            new_list.append(numbers[i])
        else:
            new_list.append(delimeter)
            new_list.append(numbers[i])
    return new_
