from typing import List


def remove_duplicates(numbers: List[int]) -> List[int]:
    """ From a list of integers, remove all elements that occur more than once.
    Keep order of elements left the same as in the input.
    >>> remove_duplicates([1, 2, 3, 2, 4])
    [1, 3, 4]
    """
    # keeping track of the visited numbers
    visited_numbers = set()
    # creating an empty list for the uniques
    unique_numbers = []
    for number in numbers:
        # if the number has not been visited
        if number not in visited_numbers:
            # add it to the visited_numbers
            visited_numbers.add(number)
            # and to the uniques
            unique_numbers.append(number)

    return unique_numbers

