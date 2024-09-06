from typing import List


def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    """ Insert a number 'delimeter' between every two consecutive elements of input list `numbers'
    >>> intersperse([], 4)
    []
    >>> intersperse([1, 2, 3], 4)
    [1, 4, 2, 4, 3]
    """

    return [
        num
        for tup in zip(numbers[::2], numbers[1::2] + (numbers[-1:],))
        for num in tup + (delimeter,)
    ][:-1]

