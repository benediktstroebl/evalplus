from typing import List


def remove_duplicates(numbers: List[int]) -> List[int]:
    """ From a list of integers, remove all elements that occur more than once.
    Keep order of elements left the same as in the input.
    >>> remove_duplicates([1, 2, 3, 2, 4])
    [1, 3, 4]
    """
    if numbers == []:
        return []
    if len(numbers) == 1:
        return numbers
    if numbers[0] not in numbers[1:]:
        return [numbers[0]] + remove_duplicates(numbers[1:])
    return remove_duplicates(numbers[1:])

