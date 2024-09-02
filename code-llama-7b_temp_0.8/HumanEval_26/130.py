from typing import List


def remove_duplicates(numbers: List[int]) -> List[int]:
    """ From a list of integers, remove all elements that occur more than once.
    Keep order of elements left the same as in the input.
    >>> remove_duplicates([1, 2, 3, 2, 4])
    [1, 3, 4]
    """
    # Counter
    # Get all the unique elements
    # https://docs.python.org/3/library/collections.html#collections.Counter
    #
    # O(n)
    # O(n)
    seen = {}
    result = []
    for n in numbers:
        if n in seen:
            seen[n] += 1
        else:
            seen[n] = 1
            result.append(n)

    return result

