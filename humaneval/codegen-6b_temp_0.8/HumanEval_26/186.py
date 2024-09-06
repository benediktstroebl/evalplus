from typing import List


def remove_duplicates(numbers: List[int]) -> List[int]:
    """ From a list of integers, remove all elements that occur more than once.
    Keep order of elements left the same as in the input.
    >>> remove_duplicates([1, 2, 3, 2, 4])
    [1, 3, 4]
    """
    if not numbers:
        return []
    target = numbers[0]
    index = 1
    while index < len(numbers):
        if numbers[index] == target:
            del numbers[index]
        else:
            target = numbers[index]
            index += 1
    return numbers

