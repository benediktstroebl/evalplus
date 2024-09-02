from typing import List


def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    """ Insert a number 'delimeter' between every two consecutive elements of input list `numbers'
    >>> intersperse([], 4)
    []
    >>> intersperse([1, 2, 3], 4)
    [1, 4, 2, 4, 3]
    """
    numbers_with_delimeter = [numbers[0]]

    if len(numbers) == 1:
        return numbers_with_delimeter

    for i in range(1, len(numbers)):
        numbers_with_delimeter.append(delimeter)
        numbers_with_delimeter.append(numbers[i])

    return numbers_with_delimeter

