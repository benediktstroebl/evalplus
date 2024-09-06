from typing import List


def remove_duplicates(numbers: List[int]) -> List[int]:
    """ From a list of integers, remove all elements that occur more than once.
    Keep order of elements left the same as in the input.
    >>> remove_duplicates([1, 2, 3, 2, 4])
    [1, 3, 4]
    """
    remove_index = 0
    for index in range(1, len(numbers)):
        if numbers[index] in numbers[0:index]:
            numbers.pop(remove_index)
            remove_index = remove_index - 1
    return numbers

