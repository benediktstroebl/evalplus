from typing import List


def remove_duplicates(numbers: List[int]) -> List[int]:
    """ From a list of integers, remove all elements that occur more than once.
    Keep order of elements left the same as in the input.
    >>> remove_duplicates([1, 2, 3, 2, 4])
    [1, 3, 4]
    """
    numbers = list(set(numbers))
    if len(numbers) < 2:
        return numbers
    for i in range(1, len(numbers)):
        if numbers[i] == numbers[i-1]:
            numbers.remove(numbers[i-1])
    return numbers

