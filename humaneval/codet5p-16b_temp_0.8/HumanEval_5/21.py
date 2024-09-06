from typing import List


def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    """ Insert a number 'delimeter' between every two consecutive elements of input list `numbers'
    >>> intersperse([], 4)
    []
    >>> intersperse([1, 2, 3], 4)
    [1, 4, 2, 4, 3]
    """

    numbers = numbers[:]  # copy input list
    insertion = 0
    while insertion < len(numbers) - 1:
        numbers[insertion], numbers[insertion + 1] = numbers[insertion + 1], delimeter
        insertion += 2
    return numbers
