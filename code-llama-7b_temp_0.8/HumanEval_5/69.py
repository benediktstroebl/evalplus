from typing import List


def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    """ Insert a number 'delimeter' between every two consecutive elements of input list `numbers'
    >>> intersperse([], 4)
    []
    >>> intersperse([1, 2, 3], 4)
    [1, 4, 2, 4, 3]
    """

    if numbers == []:
        return []

    numbers_length = len(numbers)

    # do not change numbers length, just add delimeters
    result_length = numbers_length * 2 - 1
    result = [0] * result_length

    for i in range(numbers_length):
        result[i * 2] = numbers[i]
        result[i * 2 + 1] = delimeter

    return result
