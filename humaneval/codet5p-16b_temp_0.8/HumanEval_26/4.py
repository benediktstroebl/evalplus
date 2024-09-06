from typing import List


def remove_duplicates(numbers: List[int]) -> List[int]:
    """ From a list of integers, remove all elements that occur more than once.
    Keep order of elements left the same as in the input.
    >>> remove_duplicates([1, 2, 3, 2, 4])
    [1, 3, 4]
    """

    non_duplicates = set()
    result = []
    for item in numbers:
        if item in non_duplicates:
            continue
        else:
            non_duplicates.add(item)
            result.append(item)
    return result

