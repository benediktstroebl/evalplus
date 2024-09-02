from typing import List


def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    """ Insert a number 'delimeter' between every two consecutive elements of input list `numbers'
    >>> intersperse([], 4)
    []
    >>> intersperse([1, 2, 3], 4)
    [1, 4, 2, 4, 3]
    """
    # The list can be interspersed inplace
    if len(numbers) < 2:
        return numbers
    numbers[1::2] = map(lambda x: delimeter, numbers[1::2])
    return sum(zip(numbers[::2], numbers[1::2]), [])

