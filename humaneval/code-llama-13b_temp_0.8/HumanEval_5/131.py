from typing import List


def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    """ Insert a number 'delimeter' between every two consecutive elements of input list `numbers'
    >>> intersperse([], 4)
    []
    >>> intersperse([1, 2, 3], 4)
    [1, 4, 2, 4, 3]
    """

    delimetered = []
    for index in range(len(numbers) - 1):
        delimetered.append(numbers[index])
        delimetered.append(delimeter)

    delimetered.append(numbers[-1])

    return delimetered

