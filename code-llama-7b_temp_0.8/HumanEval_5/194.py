from typing import List


def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    """ Insert a number 'delimeter' between every two consecutive elements of input list `numbers'
    >>> intersperse([], 4)
    []
    >>> intersperse([1, 2, 3], 4)
    [1, 4, 2, 4, 3]
    """

    # base case: empty list
    if len(numbers) == 0:
        return []

    # make a shallow copy of numbers
    result = numbers.copy()

    # find the middle of the list
    mid = len(result) // 2

    # insert a delimeter at the middle
    result.insert(mid, delimeter)

    # make a recursive call on the left half of the list
    result[1:mid] = intersperse(result[1:mid], delimeter)

    return result

