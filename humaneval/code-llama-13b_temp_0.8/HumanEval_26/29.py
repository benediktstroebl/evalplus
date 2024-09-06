from typing import List


def remove_duplicates(numbers: List[int]) -> List[int]:
    """ From a list of integers, remove all elements that occur more than once.
    Keep order of elements left the same as in the input.
    >>> remove_duplicates([1, 2, 3, 2, 4])
    [1, 3, 4]
    """
    # turn a list of integers into a set
    seen = set(numbers)
    # return a list of integers in the original order
    return [num for num in numbers if num in seen or seen.add(num)]
