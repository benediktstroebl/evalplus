from typing import List


def remove_duplicates(numbers: List[int]) -> List[int]:
    """ From a list of integers, remove all elements that occur more than once.
    Keep order of elements left the same as in the input.
    >>> remove_duplicates([1, 2, 3, 2, 4])
    [1, 3, 4]
    """
    # If list is empty
    if numbers == []:
        return []
    # Make a list to store the duplicate element's position
    duplicate_indices = []
    # Filter out all the duplicated elements
    numbers = [numbers[0]] + list(filter(lambda x: x != numbers[0], numbers[1:]))

    # filter duplicated indices
    for i, value in enumerate(numbers):
        duplicate_index = None
        if value in numbers[:i]:
            duplicate_index = numbers[:i].index(value)
            # if there is a duplicate element
            if duplicate_index != 0:
                duplicate_indices.append(duplicate_index)
    # filter
    numbers = list(filter(lambda x: x not in duplicate_indices, numbers))
    return numbers

