from typing import List


def remove_duplicates(numbers: List[int]) -> List[int]:
    """ From a list of integers, remove all elements that occur more than once.
    Keep order of elements left the same as in the input.
    >>> remove_duplicates([1, 2, 3, 2, 4])
    [1, 3, 4]
    """
    if not numbers:
        return []
    index = 0
    while index < len(numbers):
        if numbers[index] == numbers[index + 1]:
            del numbers[index + 1]
        else:
            index += 1
    return numbers

