from typing import List, Tuple


def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    """ From a supplied list of numbers (of length at least two) select and return two that are the closest to each
    other and return them in order (smaller number, larger number).
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2])
    (2.0, 2.2)
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0])
    (2.0, 2.0)
    """
    smallest, second_smallest = float("inf"), float("inf")
    smallest_index = 0
    second_smallest_index = 0

    for i, value in enumerate(numbers):
        if value < smallest:
            smallest = value
            smallest_index = i
        if value < second_smallest:
            second_smallest = value
            second_smallest_index = i

    return smallest, second_smallest

