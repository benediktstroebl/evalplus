from typing import List


def remove_duplicates(numbers: List[int]) -> List[int]:
    """ From a list of integers, remove all elements that occur more than once.
    Keep order of elements left the same as in the input.
    >>> remove_duplicates([1, 2, 3, 2, 4])
    [1, 3, 4]
    """
    if len(numbers) < 2:
        return numbers
    i = 0
    for j in range(len(numbers)-1):
        if numbers[j] != numbers[j+1]:
            i = j
    return numbers[:i+1]
