from typing import List


def remove_duplicates(numbers: List[int]) -> List[int]:
    """ From a list of integers, remove all elements that occur more than once.
    Keep order of elements left the same as in the input.
    >>> remove_duplicates([1, 2, 3, 2, 4])
    [1, 3, 4]
    """

    # We use a set to keep track of what numbers are already present.
    seen_numbers = set()

    # We keep track of the final list to return.
    unique_list = []

    for num in numbers:

        # We add num to the set if it is not already in the set.
        if num not in seen_numbers:
            unique_list.append(num)

        # We add num to the set, as we know it is already present.
        seen_numbers.add(num)

    return unique_list

