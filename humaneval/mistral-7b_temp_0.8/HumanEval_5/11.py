from typing import List


def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    """ Insert a number 'delimeter' between every two consecutive elements of input list `numbers'
    >>> intersperse([], 4)
    []
    >>> intersperse([1, 2, 3], 4)
    [1, 4, 2, 4, 3]
    """
    # Note that the empty list and the list of a single number cannot be reduced to the empty list, so
    # there are two base cases here.
    if len(numbers) == 0:
        return []
    if len(numbers) == 1:
        return numbers

    # Perform the "reduction" and return the final list
    return [numbers[0]] + [delimeter] + [numbers[1]] + \
           intersperse(numbers[2:], delimeter)

