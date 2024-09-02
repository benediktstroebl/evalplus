from typing import List


def remove_duplicates(numbers: List[int]) -> List[int]:
    """ From a list of integers, remove all elements that occur more than once.
    Keep order of elements left the same as in the input.
    >>> remove_duplicates([1, 2, 3, 2, 4])
    [1, 3, 4]
    """

    if len(numbers) == 0:
        return numbers
    if len(numbers) == 1:
        return numbers
    j = 0
    for i in range(1, len(numbers)):
        if numbers[i]!= numbers[j]:
            j += 1
            numbers[j] = numbers[i]
    return numbers[0:j + 1]
