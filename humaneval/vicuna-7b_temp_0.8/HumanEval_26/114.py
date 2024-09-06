from typing import List


def remove_duplicates(numbers: List[int]) -> List[int]:
    """ From a list of integers, remove all elements that occur more than once.
    Keep order of elements left the same as in the input.
    >>> remove_duplicates([1, 2, 3, 2, 4])
    [1, 3, 4]
    """
    numbers = list(numbers)
    items = len(numbers)
    for i in range(items):
        if i != numbers.index(numbers[i]):
            numbers.remove(numbers.index(numbers[i]))
    return numbers

