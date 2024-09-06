from typing import List


def remove_duplicates(numbers: List[int]) -> List[int]:
    """ From a list of integers, remove all elements that occur more than once.
    Keep order of elements left the same as in the input.
    >>> remove_duplicates([1, 2, 3, 2, 4])
    [1, 3, 4]
    """
    if not numbers:
        return []
    d = {}
    for n in numbers:
        if n not in d:
            d[n] = 0
        d[n] += 1
    d2 = [n for n in d if d[n] == 1]
    return d2

