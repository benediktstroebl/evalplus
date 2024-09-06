from typing import List


def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    """ Insert a number 'delimeter' between every two consecutive elements of input list `numbers'
    >>> intersperse([], 4)
    []
    >>> intersperse([1, 2, 3], 4)
    [1, 4, 2, 4, 3]
    """

    # intersperse() behaves differently than the corresponding function in
    # the standard library: the delimeter is not appended at the end of the
    # result list.
    # >>> intersperse([1, 2, 3], 4)
    # [1, 4, 2, 4, 3, 4]

    return [n for number in numbers for n in [number, delimeter]][:-1]

