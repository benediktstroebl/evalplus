from typing import List


def remove_duplicates(numbers: List[int]) -> List[int]:
    """ From a list of integers, remove all elements that occur more than once.
    Keep order of elements left the same as in the input.
    >>> remove_duplicates([1, 2, 3, 2, 4])
    [1, 3, 4]
    """
    # the key to this question is to have a set to store all unique values
    unique_values = set()
    new_list = []
    for num in numbers:
        if num in unique_values:
            continue
        else:
            unique_values.add(num)
            new_list.append(num)
    return new_list

