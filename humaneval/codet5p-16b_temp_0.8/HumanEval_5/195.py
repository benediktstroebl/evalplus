from typing import List


def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    """ Insert a number 'delimeter' between every two consecutive elements of input list `numbers'
    >>> intersperse([], 4)
    []
    >>> intersperse([1, 2, 3], 4)
    [1, 4, 2, 4, 3]
    """

    lst = []
    for i in range(len(numbers)-1):
        if i % 2 == 0:
            lst.append(numbers[i])
            lst.append(delimeter)
        else:
            lst.append(delimeter)
            lst.append(numbers[i])
    lst.append(numbers[-1])
    return lst

