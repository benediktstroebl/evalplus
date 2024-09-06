from typing import List


def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    """ Insert a number 'delimeter' between every two consecutive elements of input list `numbers'
    >>> intersperse([], 4)
    []
    >>> intersperse([1, 2, 3], 4)
    [1, 4, 2, 4, 3]
    """
    # Check the base case
    if len(numbers) == 1:
        return [numbers[0]]

    # Get the head and tail of the list
    head, *tail = numbers
    return head + [delimeter] + intersperse(tail, delimeter)

