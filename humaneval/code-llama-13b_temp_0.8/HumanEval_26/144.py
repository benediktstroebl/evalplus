from typing import List


def remove_duplicates(numbers: List[int]) -> List[int]:
    """ From a list of integers, remove all elements that occur more than once.
    Keep order of elements left the same as in the input.
    >>> remove_duplicates([1, 2, 3, 2, 4])
    [1, 3, 4]
    """
    # Each element can be either added to the list, or ignored.
    # We do this by keeping a separate list of "seen" elements.
    # We also keep a separate list of elements to return.
    # As we encounter each element, we check if it's in the seen list
    # If it is, we ignore it and move on. If it's not, we add it to both lists
    seen = []
    to_return = []
    for element in numbers:
        if element not in seen:
            seen.append(element)
            to_return.append(element)
    return to_return
