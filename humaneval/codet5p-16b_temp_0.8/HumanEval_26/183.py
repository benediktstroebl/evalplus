from typing import List


def remove_duplicates(numbers: List[int]) -> List[int]:
    """ From a list of integers, remove all elements that occur more than once.
    Keep order of elements left the same as in the input.
    >>> remove_duplicates([1, 2, 3, 2, 4])
    [1, 3, 4]
    """

    result = []
    unique_elements = set()
    for num in numbers:
        if num not in unique_elements:
            result.append(num)
            unique_elements.add(num)

    return result
