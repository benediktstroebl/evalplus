from typing import List


def remove_duplicates(numbers: List[int]) -> List[int]:
    """ From a list of integers, remove all elements that occur more than once.
    Keep order of elements left the same as in the input.
    >>> remove_duplicates([1, 2, 3, 2, 4])
    [1, 3, 4]
    """

    # TODO: Write your code here
    list_of_non_duplicates = []
    for number in numbers:
        if number not in list_of_non_duplicates:
            list_of_non_duplicates.append(number)

    return list_of_non_duplicates

