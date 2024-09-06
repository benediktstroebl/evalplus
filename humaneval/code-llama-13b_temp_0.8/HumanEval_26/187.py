from typing import List


def remove_duplicates(numbers: List[int]) -> List[int]:
    """ From a list of integers, remove all elements that occur more than once.
    Keep order of elements left the same as in the input.
    >>> remove_duplicates([1, 2, 3, 2, 4])
    [1, 3, 4]
    """
    #  Use a set to keep track of elements already seen
    #  and overwrite the initial list
    seen = set()
    #  Iterate backwards to avoid shifting elements
    #  (which would result in a list that is not ordered as the input)
    #  and remove elements already seen
    for i in range(len(numbers) - 1, -1, -1):
        if numbers[i] in seen:
            del numbers[i]
        else:
            seen.add(numbers[i])
    return numbers
