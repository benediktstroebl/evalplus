from typing import List


def remove_duplicates(numbers: List[int]) -> List[int]:
    """ From a list of integers, remove all elements that occur more than once.
    Keep order of elements left the same as in the input.
    >>> remove_duplicates([1, 2, 3, 2, 4])
    [1, 3, 4]
    """
    # Using list comprehension
    # return list(dict.fromkeys(numbers))
    # Using set
    # return list(set(numbers))
    # Using sort
    numbers.sort()
    i, j = 0, 1
    while j < len(numbers):
        if numbers[i] == numbers[j]:
            del numbers[j]
        else:
            i += 1
            j += 1
    return numbers

