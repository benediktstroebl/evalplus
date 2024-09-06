from typing import List


def remove_duplicates(numbers: List[int]) -> List[int]:
    """ From a list of integers, remove all elements that occur more than once.
    Keep order of elements left the same as in the input.
    >>> remove_duplicates([1, 2, 3, 2, 4])
    [1, 3, 4]
    """
    number_seen = set()
    unique = []
    for n in numbers:
        if n not in number_seen:
            number_seen.add(n)
            unique.append(n)
    return unique

