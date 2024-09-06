from typing import List


def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    """ Insert a number 'delimeter' between every two consecutive elements of input list `numbers'
    >>> intersperse([], 4)
    []
    >>> intersperse([1, 2, 3], 4)
    [1, 4, 2, 4, 3]
    """
    # This solution is faster than using list comprehension,
    # because we don't need to construct a new list of the same length as numbers
    # but the solution is not as readable as list comprehension one
    # because it's hard to read what is going on there
    if len(numbers) == 0:
        return []
    result = [numbers[0]]
    for i in range(1, len(numbers)):
        result.append(delimeter)
        result.append(numbers[i])
    return result

