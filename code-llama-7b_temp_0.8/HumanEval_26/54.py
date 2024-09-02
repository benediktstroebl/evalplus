from typing import List


def remove_duplicates(numbers: List[int]) -> List[int]:
    """ From a list of integers, remove all elements that occur more than once.
    Keep order of elements left the same as in the input.
    >>> remove_duplicates([1, 2, 3, 2, 4])
    [1, 3, 4]
    """
    # Empty list
    if not numbers:
        return []
    # Only one element in list
    elif len(numbers) == 1:
        return numbers
    # List has two or more elements
    else:
        # Loop through list
        # If first element is not the same as second element
        # Append first element to new list
        # If second element is not the same as third element
        # Append second element to new list
        # Loop until the end of the list
        new_list = []
        new_list.append(numbers[0])
        for index in range(len(numbers)):
            if numbers[index] != numbers[index - 1]:
                new_list.append(numbers[index])
        return new_list

