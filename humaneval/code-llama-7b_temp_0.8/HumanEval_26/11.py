from typing import List


def remove_duplicates(numbers: List[int]) -> List[int]:
    """ From a list of integers, remove all elements that occur more than once.
    Keep order of elements left the same as in the input.
    >>> remove_duplicates([1, 2, 3, 2, 4])
    [1, 3, 4]
    """
    if not numbers:
        return []
    last_item = numbers[0]
    new_list = [last_item]
    for item in numbers[1:]:
        if item != last_item:
            new_list.append(item)
        last_item = item
    return new_list
