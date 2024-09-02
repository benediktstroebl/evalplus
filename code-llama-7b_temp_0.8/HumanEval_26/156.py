from typing import List


def remove_duplicates(numbers: List[int]) -> List[int]:
    """ From a list of integers, remove all elements that occur more than once.
    Keep order of elements left the same as in the input.
    >>> remove_duplicates([1, 2, 3, 2, 4])
    [1, 3, 4]
    """
    occured_numbers = set()
    duplicate_numbers = set()

    for number in numbers:
        if number in occured_numbers:
            duplicate_numbers.add(number)
        else:
            occured_numbers.add(number)

    for duplicate_number in duplicate_numbers:
        numbers.remove(duplicate_number)

    return numbers
