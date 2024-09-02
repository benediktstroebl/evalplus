from typing import List


def remove_duplicates(numbers: List[int]) -> List[int]:
    """ From a list of integers, remove all elements that occur more than once.
    Keep order of elements left the same as in the input.
    >>> remove_duplicates([1, 2, 3, 2, 4])
    [1, 3, 4]
    """
    previous_element = None
    duplicate_removed_elements = []

    for element in numbers:
        if element != previous_element:
            previous_element = element
            duplicate_removed_elements.append(element)

    return duplicate_removed_elements

