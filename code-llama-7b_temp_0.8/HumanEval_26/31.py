from typing import List


def remove_duplicates(numbers: List[int]) -> List[int]:
    """ From a list of integers, remove all elements that occur more than once.
    Keep order of elements left the same as in the input.
    >>> remove_duplicates([1, 2, 3, 2, 4])
    [1, 3, 4]
    """

    if len(numbers) <= 1:
        return numbers

    list_size = len(numbers)
    first_indx = 1
    while first_indx < list_size:
        while first_indx < list_size and numbers[first_indx] != numbers[first_indx - 1]:
            first_indx += 1

        if first_indx == list_size:
            break

        while first_indx < list_size and numbers[first_indx] == numbers[first_indx - 1]:
            first_indx += 1
            list_size -= 1

    return numbers[:list_size]

