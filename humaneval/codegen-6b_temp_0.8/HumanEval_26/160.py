from typing import List


def remove_duplicates(numbers: List[int]) -> List[int]:
    """ From a list of integers, remove all elements that occur more than once.
    Keep order of elements left the same as in the input.
    >>> remove_duplicates([1, 2, 3, 2, 4])
    [1, 3, 4]
    """
    # process for all items in list
    for num in numbers:
        # check if item is not in list
        if numbers.count(num) > 1:
            # remove item
            numbers.remove(num)
    return numbers

