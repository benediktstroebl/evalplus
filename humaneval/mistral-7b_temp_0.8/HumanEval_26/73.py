from typing import List


def remove_duplicates(numbers: List[int]) -> List[int]:
    """ From a list of integers, remove all elements that occur more than once.
    Keep order of elements left the same as in the input.
    >>> remove_duplicates([1, 2, 3, 2, 4])
    [1, 3, 4]
    """
    numbers_set = set()
    return_list = []
    for n in numbers:
        if n not in numbers_set:
            numbers_set.add(n)
            return_list.append(n)
    return return_list

