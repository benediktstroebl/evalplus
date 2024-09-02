from typing import List


def remove_duplicates(numbers: List[int]) -> List[int]:
    """ From a list of integers, remove all elements that occur more than once.
    Keep order of elements left the same as in the input.
    >>> remove_duplicates([1, 2, 3, 2, 4])
    [1, 3, 4]
    """
    numbers_dict = {}
    for number in numbers:
        if number not in numbers_dict.keys():
            numbers_dict[number] = 1
        else:
            numbers_dict[number] += 1
    numbers_set = set()
    for key, value in numbers_dict.items():
        if value == 1:
            numbers_set.add(key)
    return list(numbers_set)

