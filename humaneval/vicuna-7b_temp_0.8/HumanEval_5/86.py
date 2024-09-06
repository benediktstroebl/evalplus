from typing import List


def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    """ Insert a number 'delimeter' between every two consecutive elements of input list `numbers'
    >>> intersperse([], 4)
    []
    >>> intersperse([1, 2, 3], 4)
    [1, 4, 2, 4, 3]
    """
    new_numbers = []
    i = 0
    while i < len(numbers) - 1:
        new_numbers.append(numbers[i])
        i += 1
        j = i + 1
        while j < len(numbers) and numbers[j] == numbers[i]:
            j += 1
        new_numbers.append(numbers[j])
    return new_numbers

