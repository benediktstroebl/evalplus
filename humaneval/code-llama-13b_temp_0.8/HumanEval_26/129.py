from typing import List


def remove_duplicates(numbers: List[int]) -> List[int]:
    """ From a list of integers, remove all elements that occur more than once.
    Keep order of elements left the same as in the input.
    >>> remove_duplicates([1, 2, 3, 2, 4])
    [1, 3, 4]
    """

    if len(numbers) == 0:
        return []

    duplicate_free = [numbers[0]]
    for number in numbers[1:]:
        if number not in duplicate_free:
            duplicate_free.append(number)
    return duplicate_free

