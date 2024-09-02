from typing import List


def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    """ Insert a number 'delimeter' between every two consecutive elements of input list `numbers'
    >>> intersperse([], 4)
    []
    >>> intersperse([1, 2, 3], 4)
    [1, 4, 2, 4, 3]
    """
    if not numbers:
        return []
    # numbers.insert(0, numbers[0])
    # numbers.insert(len(numbers), numbers[len(numbers) - 1])
    # numbers.insert(2, numbers[1])
    # numbers.insert(3, numbers[2])
    # numbers.insert(4, numbers[3])
    # numbers.insert(6, numbers[4])
    # numbers.insert(7, numbers[5])
    return [item for pair in zip(numbers, [delimeter] * len(numbers)) for item in pair]

