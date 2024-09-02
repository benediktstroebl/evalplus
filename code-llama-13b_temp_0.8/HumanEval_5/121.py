from typing import List


def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    """ Insert a number 'delimeter' between every two consecutive elements of input list `numbers'
    >>> intersperse([], 4)
    []
    >>> intersperse([1, 2, 3], 4)
    [1, 4, 2, 4, 3]
    """

    numbers_copy: List[int] = numbers.copy()
    if len(numbers) <= 1:
        return numbers

    # Note that we are starting loop from len(numbers)-2 to skip the last element (since we need to insert
    # a value after the last element)
    for i in range(len(numbers) - 2, -1, -1):
        numbers_copy.insert(i + 1, delimeter)
    return numbers_copy

