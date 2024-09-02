from typing import List


def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    """ Insert a number 'delimeter' between every two consecutive elements of input list `numbers'
    >>> intersperse([], 4)
    []
    >>> intersperse([1, 2, 3], 4)
    [1, 4, 2, 4, 3]
    """

    numbers_list = []
    for i in range(len(numbers) - 1):
        numbers_list.append(numbers[i])
        numbers_list.append(delimeter)
    numbers_list.append(numbers[-1])
    return numbers_list


