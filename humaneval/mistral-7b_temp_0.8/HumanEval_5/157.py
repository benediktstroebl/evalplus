from typing import List


def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    """ Insert a number 'delimeter' between every two consecutive elements of input list `numbers'
    >>> intersperse([], 4)
    []
    >>> intersperse([1, 2, 3], 4)
    [1, 4, 2, 4, 3]
    """
    lst = []
    if len(numbers) == 0:
        return []
    lst.append(numbers[0])
    for i in range(len(numbers) - 1):
        lst.append(delimeter)
        lst.append(numbers[i + 1])
    lst.append(delimeter)
    return lst

