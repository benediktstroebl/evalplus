from typing import List


def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    """ Insert a number 'delimeter' between every two consecutive elements of input list `numbers'
    >>> intersperse([], 4)
    []
    >>> intersperse([1, 2, 3], 4)
    [1, 4, 2, 4, 3]
    """

    return list(
        map(lambda x: delimeter if x == 4 else x, [*numbers, 4])[::2]
    )  # insert a delimeter between every two consecutive elements

