from typing import List


def remove_duplicates(numbers: List[int]) -> List[int]:
    """ From a list of integers, remove all elements that occur more than once.
    Keep order of elements left the same as in the input.
    >>> remove_duplicates([1, 2, 3, 2, 4])
    [1, 3, 4]
    """
    # Cleaned_list is the list that will be returned
    cleaned_list = []
    # Counter is a dictionary of how many times an integer occurs in numbers
    counter = {}
    # For every number in the list of integers
    for number in numbers:
        # If the number is not in the counter
        if number not in counter:
            # Add the number to the cleaned_list
            cleaned_list.append(number)
            # Add the number to the counter and set the value to 1
            counter[number] = 1
        # If the number is in the counter
        else:
            # If the number occurs 1 time in the counter
            if counter[number] == 1:
                # Remove the number from the cleaned_list
                cleaned_list.remove(number)
                # Remove the number from the counter
                counter.pop(number)
            # Otherwise
            else:
                # Add 1 to the counter for the number
                counter[number] += 1
    # Return the cleaned_list
    return cleaned_list
