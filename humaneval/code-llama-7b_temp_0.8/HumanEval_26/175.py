from typing import List


def remove_duplicates(numbers: List[int]) -> List[int]:
    """ From a list of integers, remove all elements that occur more than once.
    Keep order of elements left the same as in the input.
    >>> remove_duplicates([1, 2, 3, 2, 4])
    [1, 3, 4]
    """
    # run the same list backwards so we can keep track of what we have seen before
    for i in range(len(numbers) - 1, -1, -1):
        if numbers[i] in numbers[i + 1 :]:
            del numbers[i]

    return numbers

