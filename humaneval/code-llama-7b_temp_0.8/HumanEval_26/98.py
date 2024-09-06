from typing import List


def remove_duplicates(numbers: List[int]) -> List[int]:
    """ From a list of integers, remove all elements that occur more than once.
    Keep order of elements left the same as in the input.
    >>> remove_duplicates([1, 2, 3, 2, 4])
    [1, 3, 4]
    """
    # create set to store unique elements
    unique_set = set()

    # create new list to store filtered list
    filtered_list = []

    for number in numbers:
        # check if number is in set
        if number not in unique_set:
            # if not, add it
            unique_set.add(number)
            # and append it to new list
            filtered_list.append(number)

    return filtered_list

