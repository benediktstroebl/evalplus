from typing import List


def remove_duplicates(numbers: List[int]) -> List[int]:
    """ From a list of integers, remove all elements that occur more than once.
    Keep order of elements left the same as in the input.
    >>> remove_duplicates([1, 2, 3, 2, 4])
    [1, 3, 4]
    """
    # we can use a set to find duplicates
    # but we need to preserve order, so we add to list instead
    num_seen = set()
    return [num for num in numbers if num not in num_seen and not num_seen.add(num)]

