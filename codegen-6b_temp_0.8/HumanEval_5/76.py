from typing import List


def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    """ Insert a number 'delimeter' between every two consecutive elements of input list `numbers'
    >>> intersperse([], 4)
    []
    >>> intersperse([1, 2, 3], 4)
    [1, 4, 2, 4, 3]
    """
    if len(numbers) == 0:
        return numbers
    if delimeter == numbers[-1]:
        return numbers

    new_list = []
    for i in range(len(numbers) - 1):
        new_list.append(numbers[i])
        new_list.append(delimeter)
    new_list.append(numbers[-1])
    return new_list

