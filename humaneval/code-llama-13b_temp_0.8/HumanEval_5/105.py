from typing import List


def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    """ Insert a number 'delimeter' between every two consecutive elements of input list `numbers'
    >>> intersperse([], 4)
    []
    >>> intersperse([1, 2, 3], 4)
    [1, 4, 2, 4, 3]
    """
    output = []
    size = len(numbers)
    for index in range(size):
        output.append(numbers[index])
        if index < size - 1:
            output.append(delimeter)
    return output

