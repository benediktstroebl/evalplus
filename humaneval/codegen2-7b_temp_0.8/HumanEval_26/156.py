from typing import List


def remove_duplicates(numbers: List[int]) -> List[int]:
    """ From a list of integers, remove all elements that occur more than once.
    Keep order of elements left the same as in the input.
    >>> remove_duplicates([1, 2, 3, 2, 4])
    [1, 3, 4]
    """
    duplicate_marker = 0
    new_list = []

    for i, number in enumerate(numbers):
        if number!= duplicate_marker:
            new_list.append(number)
            duplicate_marker = number
        else:
            pass

    return new_list

