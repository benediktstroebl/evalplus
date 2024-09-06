from typing import List


def remove_duplicates(numbers: List[int]) -> List[int]:
    """ From a list of integers, remove all elements that occur more than once.
    Keep order of elements left the same as in the input.
    >>> remove_duplicates([1, 2, 3, 2, 4])
    [1, 3, 4]
    """
    numbers_dict = {}
    for n in numbers:
        if n in numbers_dict:
            numbers_dict[n] += 1
        else:
            numbers_dict[n] = 1
    return [n for n in numbers_dict]

