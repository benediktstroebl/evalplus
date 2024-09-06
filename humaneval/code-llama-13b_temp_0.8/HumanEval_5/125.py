from typing import List


def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    """ Insert a number 'delimeter' between every two consecutive elements of input list `numbers'
    >>> intersperse([], 4)
    []
    >>> intersperse([1, 2, 3], 4)
    [1, 4, 2, 4, 3]
    """

    if len(numbers) <= 1:
        return numbers
    numbers.append(delimeter)
    return [
        numbers[i]
        for i in range(len(numbers) - 1)
        if not (i % 2 == 1 and numbers[i] == delimeter)
    ]

