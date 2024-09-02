from typing import List


def remove_duplicates(numbers: List[int]) -> List[int]:
    """ From a list of integers, remove all elements that occur more than once.
    Keep order of elements left the same as in the input.
    >>> remove_duplicates([1, 2, 3, 2, 4])
    [1, 3, 4]
    """

    # This is not a true O(n) solution since we still iterate over the whole list
    # when we hit the second occurence of an element. But it's simple, fast and
    # works.
    return list(dict.fromkeys(numbers))
