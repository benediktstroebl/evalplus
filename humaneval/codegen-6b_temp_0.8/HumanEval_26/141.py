from typing import List


def remove_duplicates(numbers: List[int]) -> List[int]:
    """ From a list of integers, remove all elements that occur more than once.
    Keep order of elements left the same as in the input.
    >>> remove_duplicates([1, 2, 3, 2, 4])
    [1, 3, 4]
    """
    second_number = None
    new_numbers = []

    for i, number in enumerate(numbers):
        if number != second_number:
            new_numbers.append(number)
        second_number = number

    return new_numbers

