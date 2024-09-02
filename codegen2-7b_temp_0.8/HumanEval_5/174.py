from typing import List


def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    """ Insert a number 'delimeter' between every two consecutive elements of input list `numbers'
    >>> intersperse([], 4)
    []
    >>> intersperse([1, 2, 3], 4)
    [1, 4, 2, 4, 3]
    """
    if not numbers:
        return numbers

    lst = [delimeter] + numbers
    current_iter = 1
    for current in lst[1:]:
        yield lst[current_iter]
        current_iter += 1
        yield current
    yield lst[current_iter]

