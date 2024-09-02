from typing import List


def remove_duplicates(numbers: List[int]) -> List[int]:
    """ From a list of integers, remove all elements that occur more than once.
    Keep order of elements left the same as in the input.
    >>> remove_duplicates([1, 2, 3, 2, 4])
    [1, 3, 4]
    """

    if len(numbers) == 0:
        return numbers
    for i in range(len(numbers)):
        numbers[i] = numbers[i]
        for j in range(i + 1, len(numbers)):
            if numbers[i] == numbers[j]:
                numbers.pop(j)
                break
    return numbers
