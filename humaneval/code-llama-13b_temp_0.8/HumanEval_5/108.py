from typing import List


def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    """ Insert a number 'delimeter' between every two consecutive elements of input list `numbers'
    >>> intersperse([], 4)
    []
    >>> intersperse([1, 2, 3], 4)
    [1, 4, 2, 4, 3]
    """

    # We are going to splice the input list. So, we need to make a copy of the input list.
    numbers = numbers[:]
    for i in range(len(numbers) - 1, 0, -1):
        numbers.insert(i, delimeter)
    return numbers

