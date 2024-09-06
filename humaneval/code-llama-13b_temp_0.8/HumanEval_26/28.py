from typing import List


def remove_duplicates(numbers: List[int]) -> List[int]:
    """ From a list of integers, remove all elements that occur more than once.
    Keep order of elements left the same as in the input.
    >>> remove_duplicates([1, 2, 3, 2, 4])
    [1, 3, 4]
    """
    seen = set()  # Create an empty set
    for number in numbers:
        if number in seen:  # Check if number is already in seen
            seen.remove(number)  # If so, remove it.
        else:
            seen.add(number)  # If not, add it.
    return sorted(seen)

