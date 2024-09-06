from typing import List


def remove_duplicates(numbers: List[int]) -> List[int]:
    """ From a list of integers, remove all elements that occur more than once.
    Keep order of elements left the same as in the input.
    >>> remove_duplicates([1, 2, 3, 2, 4])
    [1, 3, 4]
    """
    if len(numbers) == 1:
        return numbers
    current = 0
    while current < len(numbers) - 1:
        if numbers[current] == numbers[current + 1]:
            numbers.remove(numbers[current + 1])
        else:
            current += 1
    return numbers

