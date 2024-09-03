from typing import List


def remove_duplicates(numbers: List[int]) -> List[int]:
    """ From a list of integers, remove all elements that occur more than once.
    Keep order of elements left the same as in the input.
    >>> remove_duplicates([1, 2, 3, 2, 4])
    [1, 3, 4]
    """
    # To keep order of elements left the same as in the input, we first sort the
    # input, and then go through it again to remove all duplicates.
    numbers = list(numbers)
    numbers.sort()
    return [x for x in numbers if x not in numbers]

