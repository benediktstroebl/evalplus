from typing import List


def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    """ Insert a number 'delimeter' between every two consecutive elements of input list `numbers'
    >>> intersperse([], 4)
    []
    >>> intersperse([1, 2, 3], 4)
    [1, 4, 2, 4, 3]
    """

    interspersed_numbers = []
    for i, number in enumerate(numbers):
        if i == 0:
            interspersed_numbers.append(number)
        else:
            interspersed_numbers.append(delimeter)
            interspersed_numbers.append(number)

    return interspersed_numbers

