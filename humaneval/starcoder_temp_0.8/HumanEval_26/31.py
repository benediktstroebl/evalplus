from typing import List


def remove_duplicates(numbers: List[int]) -> List[int]:
    """ From a list of integers, remove all elements that occur more than once.
    Keep order of elements left the same as in the input.
    >>> remove_duplicates([1, 2, 3, 2, 4])
    [1, 3, 4]
    """
    if not numbers:
        return []

    last_index = 1
    for i in range(1, len(numbers)):
        if numbers[i]!= numbers[last_index - 1]:
            numbers[last_index] = numbers[i]
            last_index += 1
    return numbers[:last_index]

