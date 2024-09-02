from typing import List


def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    """ Insert a number 'delimeter' between every two consecutive elements of input list `numbers'
    >>> intersperse([], 4)
    []
    >>> intersperse([1, 2, 3], 4)
    [1, 4, 2, 4, 3]
    """

    interspersed_numbers = []

    for index in range(0, len(numbers) - 1, 2):
        interspersed_numbers.append(numbers[index])
        interspersed_numbers.append(delimeter)
    interspersed_numbers.append(numbers[-1])
    return interspersed_numbers

