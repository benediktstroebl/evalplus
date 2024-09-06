from typing import List


def remove_duplicates(numbers: List[int]) -> List[int]:
    """ From a list of integers, remove all elements that occur more than once.
    Keep order of elements left the same as in the input.
    >>> remove_duplicates([1, 2, 3, 2, 4])
    [1, 3, 4]
    """
    result = []  # O(n)
    seen = set()  # O(1)
    for n in numbers:  # O(n)
        if n not in seen:  # O(1)
            result.append(n)  # O(1)
            seen.add(n)  # O(1)
    return result  # O(n)

