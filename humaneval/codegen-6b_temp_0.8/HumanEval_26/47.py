from typing import List


def remove_duplicates(numbers: List[int]) -> List[int]:
    """ From a list of integers, remove all elements that occur more than once.
    Keep order of elements left the same as in the input.
    >>> remove_duplicates([1, 2, 3, 2, 4])
    [1, 3, 4]
    """
    no_duplicate_list = []
    for elem in numbers:
        if elem not in no_duplicate_list:
            no_duplicate_list.append(elem)
    return no_duplicate_list

