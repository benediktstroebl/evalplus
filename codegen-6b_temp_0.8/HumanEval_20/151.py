from typing import List, Tuple


def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    """ From a supplied list of numbers (of length at least two) select and return two that are the closest to each
    other and return them in order (smaller number, larger number).
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2])
    (2.0, 2.2)
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0])
    (2.0, 2.0)
    """
    # The list length here must be at least 2, otherwise we are left handed and don't have the 2 closest elements
    list_length = len(numbers)
    if list_length < 2:
        raise ValueError("List length must be at least 2")

    # Find the absolute difference between each pair of elements in a list
    abs_diff = lambda a, b: abs(a - b)

    # Create a new list of the elements with the absolute differences between each pair stored in order
    # a and b are the two closest elements
    abs_diffs = [(abs_diff(a, b), a, b) for a, b in zip(numbers, numbers[1:])]

    # Sort the list of absolute differences
    abs_diffs.sort()

    # return the closest pairs of elements
    a, b = abs_diffs[0]
    return a, b

