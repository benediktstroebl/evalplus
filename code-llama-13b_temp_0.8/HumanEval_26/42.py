from typing import List


def remove_duplicates(numbers: List[int]) -> List[int]:
    """ From a list of integers, remove all elements that occur more than once.
    Keep order of elements left the same as in the input.
    >>> remove_duplicates([1, 2, 3, 2, 4])
    [1, 3, 4]
    """
    # Find the length of the list
    list_length = len(numbers)

    # Create a set
    temp_set = set()

    # Iterate from the first element to the last element
    for i in range(0, list_length):
        # If the number is not found in the set, add it to the list
        if numbers[i] not in temp_set:
            temp_set.add(numbers[i])
    return list(temp_set)

