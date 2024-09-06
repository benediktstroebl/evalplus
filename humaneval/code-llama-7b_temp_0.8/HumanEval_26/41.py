from typing import List


def remove_duplicates(numbers: List[int]) -> List[int]:
    """ From a list of integers, remove all elements that occur more than once.
    Keep order of elements left the same as in the input.
    >>> remove_duplicates([1, 2, 3, 2, 4])
    [1, 3, 4]
    """
    # Duplicate the list
    duplicates = numbers.copy()

    # Sort the list
    duplicates.sort()

    # Create a variable to keep track of the previous element
    previous_element = duplicates[0]

    # Iterate over the list, starting at index 1
    for index in range(1, len(duplicates)):
        # If the current element is different from the previous element
        if duplicates[index] != previous_element:
            # Add the current element to the new list
            numbers.append(duplicates[index])
            # Update the previous element
            previous_element = duplicates[index]

    return numbers

