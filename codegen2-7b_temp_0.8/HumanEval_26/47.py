from typing import List


def remove_duplicates(numbers: List[int]) -> List[int]:
    """ From a list of integers, remove all elements that occur more than once.
    Keep order of elements left the same as in the input.
    >>> remove_duplicates([1, 2, 3, 2, 4])
    [1, 3, 4]
    """
    i = 0
    for n in range(len(numbers)):
        if numbers[i]!= numbers[n]:
            i += 1
            numbers[i] = numbers[n]
    return numbers[:i + 1
