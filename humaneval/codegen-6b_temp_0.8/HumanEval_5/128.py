from typing import List


def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    """ Insert a number 'delimeter' between every two consecutive elements of input list `numbers'
    >>> intersperse([], 4)
    []
    >>> intersperse([1, 2, 3], 4)
    [1, 4, 2, 4, 3]
    """
    if numbers == []:
        return []

    numbers = numbers[:]
    numbers.append(delimeter)

    for i in range(0, len(numbers) - 1, 2):
        numbers[i] = numbers[i] + delimeter
    return numbers[:-1]

