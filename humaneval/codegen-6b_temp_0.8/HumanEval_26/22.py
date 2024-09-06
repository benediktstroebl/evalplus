from typing import List


def remove_duplicates(numbers: List[int]) -> List[int]:
    """ From a list of integers, remove all elements that occur more than once.
    Keep order of elements left the same as in the input.
    >>> remove_duplicates([1, 2, 3, 2, 4])
    [1, 3, 4]
    """
    # If the input is an empty list, return an empty list
    if numbers == []:
        return []

    # This list will contain all the unique values from the input list
    unique_list = []

    # Iterate through the input list
    for i in numbers:
        # Check if the value is already in the unique_list
        if i not in unique_list:
            # If it is not, append it to the unique_list
            unique_list.append(i)
            # i is now no longer needed so it can be deleted
            del i

    # Once the unique_list has been populated, return it and the duplicate values will be
    # deleted.
    return unique_list

