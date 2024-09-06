from typing import List


def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    """ Insert a number 'delimeter' between every two consecutive elements of input list `numbers'
    >>> intersperse([], 4)
    []
    >>> intersperse([1, 2, 3], 4)
    [1, 4, 2, 4, 3]
    """
    result: List[int] = []

    # To avoid modifying input list, let's use a copy
    numbers_copy = numbers[:]

    # This condition is to avoid duplicating last element
    for index, number in enumerate(numbers_copy[:-1]):
        result.append(number)
        result.append(delimeter)

    result.extend(numbers_copy[-1:])

    return result

