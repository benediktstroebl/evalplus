from typing import List


def remove_duplicates(numbers: List[int]) -> List[int]:
    """ From a list of integers, remove all elements that occur more than once.
    Keep order of elements left the same as in the input.
    >>> remove_duplicates([1, 2, 3, 2, 4])
    [1, 3, 4]
    """

    # First we sort the list so that duplicates are near each other
    numbers.sort()

    # Now we can keep track of last_unique_number to know if a number is
    # unique or not
    last_unique_number = -999999
    unique_numbers = []
    for number in numbers:
        if number!= last_unique_number:
            unique_numbers.append(number)
        last_unique_number = number
    return unique_numbers
