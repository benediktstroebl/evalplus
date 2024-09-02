from typing import List


def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    """ Insert a number 'delimeter' between every two consecutive elements of input list `numbers'
    >>> intersperse([], 4)
    []
    >>> intersperse([1, 2, 3], 4)
    [1, 4, 2, 4, 3]
    """

    interspersed_numbers = []
    for num in numbers:
        interspersed_numbers += [num, delimeter]

    interspersed_numbers.pop()
    return interspersed_numbers

