from typing import List


def remove_duplicates(numbers: List[int]) -> List[int]:
    """ From a list of integers, remove all elements that occur more than once.
    Keep order of elements left the same as in the input.
    >>> remove_duplicates([1, 2, 3, 2, 4])
    [1, 3, 4]
    """
    result = []
    seen_before = set()
    for n in numbers:
        if n not in seen_before:
            seen_before.add(n)
            result.append(n)
    return
