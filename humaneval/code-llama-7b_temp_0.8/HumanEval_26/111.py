from typing import List


def remove_duplicates(numbers: List[int]) -> List[int]:
    """ From a list of integers, remove all elements that occur more than once.
    Keep order of elements left the same as in the input.
    >>> remove_duplicates([1, 2, 3, 2, 4])
    [1, 3, 4]
    """
    res: List[int] = []
    res_set: List[int] = []
    for num in numbers:
        if num not in res_set:
            res.append(num)
            res_set.append(num)

    return res
