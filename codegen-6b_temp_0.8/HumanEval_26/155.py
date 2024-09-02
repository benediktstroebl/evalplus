from typing import List


def remove_duplicates(numbers: List[int]) -> List[int]:
    """ From a list of integers, remove all elements that occur more than once.
    Keep order of elements left the same as in the input.
    >>> remove_duplicates([1, 2, 3, 2, 4])
    [1, 3, 4]
    """
    if len(numbers) < 2:
        return numbers

    new_list = []
    last = None
    for num in numbers:
        if num != last:
            last = num
            new_list.append(num)
    return new_list
