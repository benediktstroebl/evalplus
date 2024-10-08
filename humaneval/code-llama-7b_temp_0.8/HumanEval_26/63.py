from typing import List


def remove_duplicates(numbers: List[int]) -> List[int]:
    """ From a list of integers, remove all elements that occur more than once.
    Keep order of elements left the same as in the input.
    >>> remove_duplicates([1, 2, 3, 2, 4])
    [1, 3, 4]
    """
    # put duplicate elements into a set
    unique_numbers = set()
    for number in numbers:
        if number not in unique_numbers:
            unique_numbers.add(number)
    return unique_numbers
