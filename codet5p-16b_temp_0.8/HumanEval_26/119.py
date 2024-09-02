from typing import List


def remove_duplicates(numbers: List[int]) -> List[int]:
    """ From a list of integers, remove all elements that occur more than once.
    Keep order of elements left the same as in the input.
    >>> remove_duplicates([1, 2, 3, 2, 4])
    [1, 3, 4]
    """

    temp_list = []
    for i in range(len(numbers)):
        if numbers[i] not in temp_list:
            temp_list.append(numbers[i])
    return temp_list

