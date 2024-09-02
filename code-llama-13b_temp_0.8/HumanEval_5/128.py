from typing import List


def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    """ Insert a number 'delimeter' between every two consecutive elements of input list `numbers'
    >>> intersperse([], 4)
    []
    >>> intersperse([1, 2, 3], 4)
    [1, 4, 2, 4, 3]
    """

    if len(numbers) == 0:
        return []
    if len(numbers) == 1:
        return [numbers[0]]

    intersperse_list = []
    for i in range(0, len(numbers) - 1):
        intersperse_list.append(numbers[i])
        intersperse_list.append(delimeter)
    intersperse_list.append(numbers[-1])

    return intersperse_list

