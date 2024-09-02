from typing import List


def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    """ Insert a number 'delimeter' between every two consecutive elements of input list `numbers'
    >>> intersperse([], 4)
    []
    >>> intersperse([1, 2, 3], 4)
    [1, 4, 2, 4, 3]
    """

    out_list = []

    for index in range(len(numbers)):
        out_list.append(numbers[index])
        if index < (len(numbers) - 1):
            out_list.append(delimeter)

    return out_list

