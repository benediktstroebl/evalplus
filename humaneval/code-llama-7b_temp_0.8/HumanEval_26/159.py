from typing import List


def remove_duplicates(numbers: List[int]) -> List[int]:
    """ From a list of integers, remove all elements that occur more than once.
    Keep order of elements left the same as in the input.
    >>> remove_duplicates([1, 2, 3, 2, 4])
    [1, 3, 4]
    """
    set_ = set()
    list_ = []
    for i in range(len(numbers)):
        if numbers[i] in set_:
            continue
        set_.add(numbers[i])
        list_.append(numbers[i])
    return list_
