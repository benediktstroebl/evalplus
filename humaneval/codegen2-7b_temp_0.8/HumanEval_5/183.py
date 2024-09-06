from typing import List


def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    """ Insert a number 'delimeter' between every two consecutive elements of input list `numbers'
    >>> intersperse([], 4)
    []
    >>> intersperse([1, 2, 3], 4)
    [1, 4, 2, 4, 3]
    """
    if not numbers:
        return numbers

    n = len(numbers)

    if delimeter == 0:
        return numbers

    for i in range(1, n + 1):
        numbers[n - i] = delimeter
    return numbers[::-1
