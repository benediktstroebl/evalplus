from typing import List


def remove_duplicates(numbers: List[int]) -> List[int]:
    """ From a list of integers, remove all elements that occur more than once.
    Keep order of elements left the same as in the input.
    >>> remove_duplicates([1, 2, 3, 2, 4])
    [1, 3, 4]
    """
    # Brute force
    # return list(set(numbers))

    # Optimized
    i = 0
    while i < len(numbers) - 1:
        if numbers[i] == numbers[i + 1]:
            del numbers[i]
        else:
            i += 1
    return numbers

