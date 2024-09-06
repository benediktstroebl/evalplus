from typing import List


def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    """ Insert a number 'delimeter' between every two consecutive elements of input list `numbers'
    >>> intersperse([], 4)
    []
    >>> intersperse([1, 2, 3], 4)
    [1, 4, 2, 4, 3]
    """

    numbers.insert(0, 0)
    numbers.append(0)
    list_length = len(numbers)
    return [
        numbers[i] if i % 2 == 0 else delimeter
        for i in range(list_length)
    ]

