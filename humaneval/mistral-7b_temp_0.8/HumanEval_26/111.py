from typing import List


def remove_duplicates(numbers: List[int]) -> List[int]:
    """ From a list of integers, remove all elements that occur more than once.
    Keep order of elements left the same as in the input.
    >>> remove_duplicates([1, 2, 3, 2, 4])
    [1, 3, 4]
    """
    # Remove all but the first occurrence of each element
    for i in range(len(numbers)):
        if i != len(numbers) - 1 and numbers[i] == numbers[i + 1]:
            del numbers[i]
    return numbers

