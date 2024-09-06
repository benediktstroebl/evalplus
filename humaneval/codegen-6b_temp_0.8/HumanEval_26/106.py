from typing import List


def remove_duplicates(numbers: List[int]) -> List[int]:
    """ From a list of integers, remove all elements that occur more than once.
    Keep order of elements left the same as in the input.
    >>> remove_duplicates([1, 2, 3, 2, 4])
    [1, 3, 4]
    """
    if not numbers:
        return []
    result = []
    number = numbers[0]  # Store first element
    for i in range(1, len(numbers)):
        if numbers[i] == number:  # If element is a duplicate of the currently examined, skip it
            continue
        result.append(number)  # If element is not a duplicate of the currently examined, add it to the result
        number = numbers[i]  # And store the new element
    result.append(number)  # At the end, add the last element of the list
    return result

