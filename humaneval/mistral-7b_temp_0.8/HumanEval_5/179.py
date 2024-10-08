from typing import List


def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    """ Insert a number 'delimeter' between every two consecutive elements of input list `numbers'
    >>> intersperse([], 4)
    []
    >>> intersperse([1, 2, 3], 4)
    [1, 4, 2, 4, 3]
    """
    numbers_with_delimeter = []

    if not numbers:
        return numbers_with_delimeter

    numbers_with_delimeter.append(numbers[0])

    for number in numbers[1:]:
        numbers_with_delimeter.append(delimeter)
        numbers_with_delimeter.append(number)

    return numbers_with_delimeter

