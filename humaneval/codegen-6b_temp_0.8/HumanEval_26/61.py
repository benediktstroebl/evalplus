from typing import List


def remove_duplicates(numbers: List[int]) -> List[int]:
    """ From a list of integers, remove all elements that occur more than once.
    Keep order of elements left the same as in the input.
    >>> remove_duplicates([1, 2, 3, 2, 4])
    [1, 3, 4]
    """
    # 1) create a new list, starting with -1.
    # 2) keep a count of the number of appearances
    # 3) if count is 1, add the number to new list
    # 4) if count is more than 1, add the number to new list, and decrement count.

    if len(numbers) == 0:
        return numbers
    new_list = [-1]
    for number in numbers:
        if new_list[-1] != number:
            new_list.append(number)
    return new_list

