from typing import List


def remove_duplicates(numbers: List[int]) -> List[int]:
    """ From a list of integers, remove all elements that occur more than once.
    Keep order of elements left the same as in the input.
    >>> remove_duplicates([1, 2, 3, 2, 4])
    [1, 3, 4]
    """

    if not numbers:
        return []

    numbers_dict = {num: 0 for num in numbers}

    for num in numbers:
        if numbers_dict[num] == 0:
            numbers_dict[num] = 1
        else:
            del numbers_dict[num]

    return list(numbers_dict.keys())

