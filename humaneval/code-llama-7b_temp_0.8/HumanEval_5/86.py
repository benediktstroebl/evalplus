from typing import List


def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    """ Insert a number 'delimeter' between every two consecutive elements of input list `numbers'
    >>> intersperse([], 4)
    []
    >>> intersperse([1, 2, 3], 4)
    [1, 4, 2, 4, 3]
    """
    output: List[int] = []
    output.extend(numbers)
    for i in range(len(output) - 1):
        output.insert(i * 2 + 1, delimeter)
    return output
