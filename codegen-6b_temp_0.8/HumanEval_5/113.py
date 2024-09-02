from typing import List


def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    """ Insert a number 'delimeter' between every two consecutive elements of input list `numbers'
    >>> intersperse([], 4)
    []
    >>> intersperse([1, 2, 3], 4)
    [1, 4, 2, 4, 3]
    """
    if len(numbers) == 0:
        return []

    nums = []
    for i in range(0, len(numbers), 2):
        nums.append(numbers[i])
        nums.append(delimeter)
        nums.append(numbers[i + 1])
    nums.append(numbers[-1])

    return nums

