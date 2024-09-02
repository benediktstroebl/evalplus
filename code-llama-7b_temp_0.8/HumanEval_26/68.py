from typing import List


def remove_duplicates(numbers: List[int]) -> List[int]:
    """ From a list of integers, remove all elements that occur more than once.
    Keep order of elements left the same as in the input.
    >>> remove_duplicates([1, 2, 3, 2, 4])
    [1, 3, 4]
    """
    if not numbers:
        return []
    result = []
    prev = numbers[0]
    result.append(prev)
    for cur in numbers[1:]:
        if cur != prev:
            result.append(cur)
            prev = cur
    return result

