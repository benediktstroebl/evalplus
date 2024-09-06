from typing import List


def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    """ Insert a number 'delimeter' between every two consecutive elements of input list `numbers'
    >>> intersperse([], 4)
    []
    >>> intersperse([1, 2, 3], 4)
    [1, 4, 2, 4, 3]
    """
    output = []

    for index, item in enumerate(numbers):
        if index == 0:
            output.append(item)
        else:
            output.append(delimeter)
            output.append(item)

    return output

