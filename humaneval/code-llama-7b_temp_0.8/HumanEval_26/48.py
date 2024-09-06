from typing import List


def remove_duplicates(numbers: List[int]) -> List[int]:
    """ From a list of integers, remove all elements that occur more than once.
    Keep order of elements left the same as in the input.
    >>> remove_duplicates([1, 2, 3, 2, 4])
    [1, 3, 4]
    """

    # check input
    if not isinstance(numbers, list):
        return []
    for number in numbers:
        if not isinstance(number, int):
            return []

    # get length of list
    length_of_list = len(numbers)

    # empty list
    unique_list = []

    # loop over list
    for i in range(0, length_of_list):

        # if list is empty, add to list
        if len(unique_list) == 0:
            unique_list.append(numbers[i])

        # if last element of list is not equal to current element, add to list
        elif unique_list[-1] != numbers[i]:
            unique_list.append(numbers[i])

    return unique_list
