from typing import List


def remove_duplicates(numbers: List[int]) -> List[int]:
    """ From a list of integers, remove all elements that occur more than once.
    Keep order of elements left the same as in the input.
    >>> remove_duplicates([1, 2, 3, 2, 4])
    [1, 3, 4]
    """
    non_duplicate_list = []
    for n in numbers:
        if n not in non_duplicate_list:
            non_duplicate_list.append(n)
    return non_duplicate_list

