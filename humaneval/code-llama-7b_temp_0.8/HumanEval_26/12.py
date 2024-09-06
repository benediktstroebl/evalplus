from typing import List


def remove_duplicates(numbers: List[int]) -> List[int]:
    """ From a list of integers, remove all elements that occur more than once.
    Keep order of elements left the same as in the input.
    >>> remove_duplicates([1, 2, 3, 2, 4])
    [1, 3, 4]
    """
    # For every element in the input array, if the element is
    # not seen before, then add it to the output list
    result = []
    seen = set()
    for element in numbers:
        if element not in seen:
            result.append(element)
            seen.add(element)
    return result

