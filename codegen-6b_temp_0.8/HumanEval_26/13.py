from typing import List


def remove_duplicates(numbers: List[int]) -> List[int]:
    """ From a list of integers, remove all elements that occur more than once.
    Keep order of elements left the same as in the input.
    >>> remove_duplicates([1, 2, 3, 2, 4])
    [1, 3, 4]
    """
    if len(numbers) > 0:
        return_list = []
        last_item = numbers[0]
        for item in numbers:
            if item == last_item:
                continue
            return_list.append(item)
            last_item = item
        return return_list
    else:
        return []

