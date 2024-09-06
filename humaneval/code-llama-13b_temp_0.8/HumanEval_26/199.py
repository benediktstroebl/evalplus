from typing import List


def remove_duplicates(numbers: List[int]) -> List[int]:
    """ From a list of integers, remove all elements that occur more than once.
    Keep order of elements left the same as in the input.
    >>> remove_duplicates([1, 2, 3, 2, 4])
    [1, 3, 4]
    """
    numbers_clean: List[int] = []
    for i in numbers:
        if i not in numbers_clean:
            numbers_clean.append(i)
        else:
            pass
    return numbers_clean
