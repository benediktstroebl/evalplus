from typing import List


def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    """ Insert a number 'delimeter' between every two consecutive elements of input list `numbers'
    >>> intersperse([], 4)
    []
    >>> intersperse([1, 2, 3], 4)
    [1, 4, 2, 4, 3]
    """

    # Base Case: Empty List, Return Empty List
    if not numbers:
        return []

    # Recursive Case: Insert the delimeter in between two consecutive numbers
    return [numbers[0], delimeter] + intersperse(numbers[1:], delimeter)

