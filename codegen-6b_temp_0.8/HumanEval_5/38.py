from typing import List


def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    """ Insert a number 'delimeter' between every two consecutive elements of input list `numbers'
    >>> intersperse([], 4)
    []
    >>> intersperse([1, 2, 3], 4)
    [1, 4, 2, 4, 3]
    """
    inter = []
    for i in range(0, len(numbers) - 1, 2):
        inter.append(numbers[i])
        inter.append(delimeter)
        inter.append(numbers[i + 1])

    return inter + [numbers[-1]]

