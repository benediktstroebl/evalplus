from typing import List


def remove_duplicates(numbers: List[int]) -> List[int]:
    """ From a list of integers, remove all elements that occur more than once.
    Keep order of elements left the same as in the input.
    >>> remove_duplicates([1, 2, 3, 2, 4])
    [1, 3, 4]
    """
    # Initialize a dictionary to hold key value pairs.
    d = {}
    for num in numbers:
        # If num is already in the dictionary, then remove it.
        if num in d:
            d.pop(num)
        # If num is not in the dictionary, then add it.
        else:
            d[num] = True

    return list(d.keys())

