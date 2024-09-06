from typing import List


def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    """ Insert a number 'delimeter' between every two consecutive elements of input list `numbers'
    >>> intersperse([], 4)
    []
    >>> intersperse([1, 2, 3], 4)
    [1, 4, 2, 4, 3]
    """
    return [delimeter].join([str(i) for i in numbers]).split("4")


    "input_1": [1, 2, 3, 4, 5],
    "input_2": [5, 5, 5, 5, 5],
    "input_3": [1, 2, 3, 4, 5, 6, 7, 8],
    "input_4": [],

