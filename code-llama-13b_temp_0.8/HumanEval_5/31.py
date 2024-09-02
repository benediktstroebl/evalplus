from typing import List


def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    """ Insert a number 'delimeter' between every two consecutive elements of input list `numbers'
    >>> intersperse([], 4)
    []
    >>> intersperse([1, 2, 3], 4)
    [1, 4, 2, 4, 3]
    """

    ret_list: List[int] = []
    for i in range(len(numbers) - 1):
        ret_list.append(numbers[i])
        ret_list.append(delimeter)
    ret_list.append(numbers[-1])

    return ret_list

