from typing import List


def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    """ Insert a number 'delimeter' between every two consecutive elements of input list `numbers'
    >>> intersperse([], 4)
    []
    >>> intersperse([1, 2, 3], 4)
    [1, 4, 2, 4, 3]
    """
    n = len(numbers)
    if n < 2:
        return numbers
    delimeter_pos = n - 1
    for i in range(n - 1):
        numbers[delimeter_pos] = delimeter
        delimeter_pos -= 1
    return numbers

