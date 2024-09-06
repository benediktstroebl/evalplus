from typing import List


def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    """ Insert a number 'delimeter' between every two consecutive elements of input list `numbers'
    >>> intersperse([], 4)
    []
    >>> intersperse([1, 2, 3], 4)
    [1, 4, 2, 4, 3]
    """
    return list(
        (str(numbers[x]) if x == 0 or x == len(numbers) - 1 else (str(numbers[x - 1]) + str(delimeter) + str(numbers[x]))) for x in range(len(numbers))
    )

