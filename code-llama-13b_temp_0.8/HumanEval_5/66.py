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
    if len(numbers) == 1:
        return [numbers[0]]

    numbers = [numbers[0]] + numbers[1:]
    numbers = [numbers[i] if i % 2 == 0 else [delimeter, numbers[i]] for i in range(len(numbers))]
    return [item for sublist in numbers for item in sublist]

