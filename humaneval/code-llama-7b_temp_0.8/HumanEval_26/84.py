from typing import List


def remove_duplicates(numbers: List[int]) -> List[int]:
    """ From a list of integers, remove all elements that occur more than once.
    Keep order of elements left the same as in the input.
    >>> remove_duplicates([1, 2, 3, 2, 4])
    [1, 3, 4]
    """
    seen = {}

    for number in numbers:
        if number not in seen:
            seen[number] = 1
        else:
            seen[number] += 1

    return [number for number in numbers if seen[number] == 1]
