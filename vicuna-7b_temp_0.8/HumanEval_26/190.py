from typing import List


def remove_duplicates(numbers: List[int]) -> List[int]:
    """ From a list of integers, remove all elements that occur more than once.
    Keep order of elements left the same as in the input.
    >>> remove_duplicates([1, 2, 3, 2, 4])
    [1, 3, 4]
    """
    numbers = list(numbers)
    for i in range(1, len(numbers)):
        for j in range(i):
            if numbers[i] == numbers[j]:
                numbers.remove(numbers[j])
    return numbers

