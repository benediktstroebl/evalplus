from typing import List


def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    """ Insert a number 'delimeter' between every two consecutive elements of input list `numbers'
    >>> intersperse([], 4)
    []
    >>> intersperse([1, 2, 3], 4)
    [1, 4, 2, 4, 3]
    """
    new_numbers = []
    while numbers:
        new_numbers.append(numbers.pop(0))
        if numbers:
            new_numbers.append(delimeter)
    return new_numbers

assert intersperse([], 4) == []
assert intersperse([1, 2, 3], 4) == [1, 4, 2, 4, 3]

