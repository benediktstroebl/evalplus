from typing import List


def remove_duplicates(numbers: List[int]) -> List[int]:
    """ From a list of integers, remove all elements that occur more than once.
    Keep order of elements left the same as in the input.
    >>> remove_duplicates([1, 2, 3, 2, 4])
    [1, 3, 4]
    """

    i, n = 0, len(numbers)
    while i < n - 1:
        j = i + 1
        while j < n:
            if numbers[i] == numbers[j]:
                numbers.pop(j)
                n -= 1
            else:
                j += 1
        i += 1
    return numbers

