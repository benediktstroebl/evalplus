from typing import List


def remove_duplicates(numbers: List[int]) -> List[int]:
    """ From a list of integers, remove all elements that occur more than once.
    Keep order of elements left the same as in the input.
    >>> remove_duplicates([1, 2, 3, 2, 4])
    [1, 3, 4]
    """
    if not numbers:
        return []
    i = 0
    for num in numbers:
        if i < 1 or num != numbers[i - 1]:
            numbers[i] = num
            i += 1

    return numbers[:i]

