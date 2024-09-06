from typing import List


def remove_duplicates(numbers: List[int]) -> List[int]:
    """ From a list of integers, remove all elements that occur more than once.
    Keep order of elements left the same as in the input.
    >>> remove_duplicates([1, 2, 3, 2, 4])
    [1, 3, 4]
    """
    # (Re-)comparing each item to the one before it and removing
    # them if they are the same.
    if len(numbers) == 0:
        return numbers
    unique_numbers = [numbers[0]]
    for i in range(1, len(numbers)):
        if unique_numbers[-1] != numbers[i]:
            unique_numbers.append(numbers[i])
    return unique_numbers

