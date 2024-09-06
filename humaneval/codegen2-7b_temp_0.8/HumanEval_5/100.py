from typing import List


def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    """ Insert a number 'delimeter' between every two consecutive elements of input list `numbers'
    >>> intersperse([], 4)
    []
    >>> intersperse([1, 2, 3], 4)
    [1, 4, 2, 4, 3]
    """
    numbers = list(numbers)

    for i in range(len(numbers)):
        if i > 0 and numbers[i]!= numbers[i - 1]:
            numbers.insert(i, delimeter)
            i += 1

    return
