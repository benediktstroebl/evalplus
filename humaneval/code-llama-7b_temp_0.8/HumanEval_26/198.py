from typing import List


def remove_duplicates(numbers: List[int]) -> List[int]:
    """ From a list of integers, remove all elements that occur more than once.
    Keep order of elements left the same as in the input.
    >>> remove_duplicates([1, 2, 3, 2, 4])
    [1, 3, 4]
    """
    # O(n * log n)
    numbers.sort()

    # O(n)
    last_seen = None
    for index, value in enumerate(numbers):
        if last_seen is None:
            last_seen = value
        elif last_seen == value:
            numbers.pop(index)
        else:
            last_seen = value

    return numbers

