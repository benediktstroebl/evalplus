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
    relist = []
    for i, _ in enumerate(numbers):
        if i == 0:
            relist.append(numbers[0])
        elif i == len(numbers) - 1:
            relist.append(numbers[i])
        else:
            relist.append(delimeter)
            relist.append(numbers[i])

    return relist

