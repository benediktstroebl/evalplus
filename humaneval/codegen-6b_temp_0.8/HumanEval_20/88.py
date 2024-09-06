from typing import List, Tuple


def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    """ From a supplied list of numbers (of length at least two) select and return two that are the closest to each
    other and return them in order (smaller number, larger number).
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2])
    (2.0, 2.2)
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0])
    (2.0, 2.0)
    """
    # For each item in the array, compute the diff with previous and next item.
    # Sort the diffs and return the first two (closest to each other).
    first_two = sorted([(numbers[i]-numbers[i-1], i) for i in range(1, len(numbers))])
    return first_two[0][1], first_two[1][1]

