from typing import List


def remove_duplicates(numbers: List[int]) -> List[int]:
    """ From a list of integers, remove all elements that occur more than once.
    Keep order of elements left the same as in the input.
    >>> remove_duplicates([1, 2, 3, 2, 4])
    [1, 3, 4]
    """
    # Recursive solution:
    # return _remove_duplicates(numbers, [])

    # Iterative solution:
    result = []
    for x in numbers:
        if x not in result:
            result.append(x)
    return result

