from typing import List


def remove_duplicates(numbers: List[int]) -> List[int]:
    """ From a list of integers, remove all elements that occur more than once.
    Keep order of elements left the same as in the input.
    >>> remove_duplicates([1, 2, 3, 2, 4])
    [1, 3, 4]
    """
    # list to hold the unique numbers
    unique_numbers = []
    # iterate over the numbers list
    for number in numbers:
        # check if the current number is already in the list of unique numbers
        if number not in unique_numbers:
            unique_numbers.append(number)
    return unique_numbers

