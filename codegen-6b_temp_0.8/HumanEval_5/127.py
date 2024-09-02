from typing import List


def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    """ Insert a number 'delimeter' between every two consecutive elements of input list `numbers'
    >>> intersperse([], 4)
    []
    >>> intersperse([1, 2, 3], 4)
    [1, 4, 2, 4, 3]
    """
    if numbers == []:
        return []
    l = []
    for i in range(1, len(numbers)):
        l.append(numbers[i - 1])
        l.append(delimeter)
        l.append(numbers[i])
    l.append(numbers[-1])
    return l

