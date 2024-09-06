from typing import List


def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    """ Insert a number 'delimeter' between every two consecutive elements of input list `numbers'
    >>> intersperse([], 4)
    []
    >>> intersperse([1, 2, 3], 4)
    [1, 4, 2, 4, 3]
    """
    numbers.append(delimeter)
    length = len(numbers)
    for i in range(length - 1):
        numbers[i] = numbers[i + 1]
    numbers.pop()
    return numbers

