from typing import List


def remove_duplicates(numbers: List[int]) -> List[int]:
    """ From a list of integers, remove all elements that occur more than once.
    Keep order of elements left the same as in the input.
    >>> remove_duplicates([1, 2, 3, 2, 4])
    [1, 3, 4]
    """
    remaining_items = []
    unique_items = set()
    # O(n)
    for item in numbers:
        if item in unique_items:
            continue
        else:
            remaining_items.append(item)
            unique_items.add(item)
    # O(n)
    return remaining_items

