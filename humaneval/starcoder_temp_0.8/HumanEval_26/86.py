from typing import List


def remove_duplicates(numbers: List[int]) -> List[int]:
    """ From a list of integers, remove all elements that occur more than once.
    Keep order of elements left the same as in the input.
    >>> remove_duplicates([1, 2, 3, 2, 4])
    [1, 3, 4]
    """

    # We'll use a set here. It's a data structure that
    # allows no duplicates, and has a "quick lookup".
    unique_numbers = set()

    # This loop is easy: append the unique elements to
    # the new list.
    for number in numbers:
        if number not in unique_numbers:
            unique_numbers.add(number)

    # We need to convert back from the set to a list.
    return list(unique_numbers)

