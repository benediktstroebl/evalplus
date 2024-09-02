from typing import List


def remove_duplicates(numbers: List[int]) -> List[int]:
    """ From a list of integers, remove all elements that occur more than once.
    Keep order of elements left the same as in the input.
    >>> remove_duplicates([1, 2, 3, 2, 4])
    [1, 3, 4]
    """
    numbers.sort()
    result = []
    for i, number in enumerate(numbers):
        if i == 0 or number!= numbers[i - 1]:
            result.append(number)
    return
