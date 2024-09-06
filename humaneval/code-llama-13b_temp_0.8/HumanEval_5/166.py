from typing import List


def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    """ Insert a number 'delimeter' between every two consecutive elements of input list `numbers'
    >>> intersperse([], 4)
    []
    >>> intersperse([1, 2, 3], 4)
    [1, 4, 2, 4, 3]
    """

    delimeter = [delimeter]
    return [
        num
        for nums in list(zip(numbers, [delimeter * len(numbers[:-1])]))
        for num in nums
    ][::2]

