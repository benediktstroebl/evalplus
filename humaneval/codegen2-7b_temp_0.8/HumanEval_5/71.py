from typing import List


def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    """ Insert a number 'delimeter' between every two consecutive elements of input list `numbers'
    >>> intersperse([], 4)
    []
    >>> intersperse([1, 2, 3], 4)
    [1, 4, 2, 4, 3]
    """
    interspersed = []
    for i in range(len(numbers)):
        if i == 0 or numbers[i-1]!= numbers[i]:
            interspersed.append(numbers[i])
        else:
            interspersed.append(delimeter)
    return interspers
