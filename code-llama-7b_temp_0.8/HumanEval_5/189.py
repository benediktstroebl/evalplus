from typing import List


def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    """ Insert a number 'delimeter' between every two consecutive elements of input list `numbers'
    >>> intersperse([], 4)
    []
    >>> intersperse([1, 2, 3], 4)
    [1, 4, 2, 4, 3]
    """
    numbers.insert(0, numbers[0])
    numbers.insert(1, delimeter)
    numbers.insert(-1, numbers[-1])
    numbers.insert(-1, delimeter)
    return numbers[::2]

