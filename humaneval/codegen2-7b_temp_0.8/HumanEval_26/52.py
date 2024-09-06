from typing import List


def remove_duplicates(numbers: List[int]) -> List[int]:
    """ From a list of integers, remove all elements that occur more than once.
    Keep order of elements left the same as in the input.
    >>> remove_duplicates([1, 2, 3, 2, 4])
    [1, 3, 4]
    """
    removed_numbers = []
    for i in range(len(numbers)):
        if i == 0 or numbers[i]!= numbers[i - 1]:
            removed_numbers.append(numbers[i])

    return removed_
