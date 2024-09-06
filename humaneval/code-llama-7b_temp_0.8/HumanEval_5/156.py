from typing import List


def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    """ Insert a number 'delimeter' between every two consecutive elements of input list `numbers'
    >>> intersperse([], 4)
    []
    >>> intersperse([1, 2, 3], 4)
    [1, 4, 2, 4, 3]
    """
    if len(numbers) <= 1:
        return numbers

    interspered_list: List[int] = []
    for i in range(0, len(numbers) - 1):
        interspered_list += [numbers[i], delimeter]

    interspered_list += [numbers[-1]]

    return interspered_list

