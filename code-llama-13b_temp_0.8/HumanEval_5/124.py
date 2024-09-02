from typing import List


def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    """ Insert a number 'delimeter' between every two consecutive elements of input list `numbers'
    >>> intersperse([], 4)
    []
    >>> intersperse([1, 2, 3], 4)
    [1, 4, 2, 4, 3]
    """
    numbers_with_delimeter = []
    for index in range(len(numbers)):
        if index == 0:
            numbers_with_delimeter.append(numbers[index])
        else:
            numbers_with_delimeter.append(delimeter)
            numbers_with_delimeter.append(numbers[index])

    return numbers_with_delimeter

