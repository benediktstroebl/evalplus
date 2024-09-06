from typing import List


def remove_duplicates(numbers: List[int]) -> List[int]:
    """ From a list of integers, remove all elements that occur more than once.
    Keep order of elements left the same as in the input.
    >>> remove_duplicates([1, 2, 3, 2, 4])
    [1, 3, 4]
    """

    index = 0
    while index < len(numbers) - 1:
        if numbers[index] == numbers[index + 1]:
            numbers.pop(index)
        else:
            index += 1
    return numbers

