from typing import List


def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    """ Insert a number 'delimeter' between every two consecutive elements of input list `numbers'
    >>> intersperse([], 4)
    []
    >>> intersperse([1, 2, 3], 4)
    [1, 4, 2, 4, 3]
    """
    if not numbers:
        return []

    numbers_len = len(numbers)
    interspersed_numbers = [numbers[0]]
    for index in range(1, numbers_len):
        interspersed_numbers.append(delimeter)
        interspersed_numbers.append(numbers[index])

    return interspersed_numbers

