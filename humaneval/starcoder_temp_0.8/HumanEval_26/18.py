from typing import List


def remove_duplicates(numbers: List[int]) -> List[int]:
    """ From a list of integers, remove all elements that occur more than once.
    Keep order of elements left the same as in the input.
    >>> remove_duplicates([1, 2, 3, 2, 4])
    [1, 3, 4]
    """

    # Define a new empty list
    final_list = []

    # Loop over the original list
    for i in numbers:
        # Check if the element is not in the final list
        if i not in final_list:
            # Add the element to the final list
            final_list.append(i)

    return final_list

