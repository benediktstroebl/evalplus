from typing import List


def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    """ Insert a number 'delimeter' between every two consecutive elements of input list `numbers'
    >>> intersperse([], 4)
    []
    >>> intersperse([1, 2, 3], 4)
    [1, 4, 2, 4, 3]
    """

    result = []

    for index in range(len(numbers) + len(numbers) - 1):
        try:
            result.append(numbers[index])
        except IndexError:
            break
        if index % 2 == 0:
            result.append(delimeter)

    return result

