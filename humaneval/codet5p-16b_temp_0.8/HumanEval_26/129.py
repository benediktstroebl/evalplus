from typing import List


def remove_duplicates(numbers: List[int]) -> List[int]:
    """ From a list of integers, remove all elements that occur more than once.
    Keep order of elements left the same as in the input.
    >>> remove_duplicates([1, 2, 3, 2, 4])
    [1, 3, 4]
    """

    if not numbers:
        return numbers
    elif len(numbers) == 1:
        return numbers
    else:
        if numbers[0] in numbers[1:]:
            numbers = remove_duplicates(numbers[1:])
        else:
            numbers = [numbers[0]] + remove_duplicates(numbers[1:])
    return numbers

