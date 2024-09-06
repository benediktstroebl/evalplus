from typing import List, Tuple


def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    """ From a supplied list of numbers (of length at least two) select and return two that are the closest to each
    other and return them in order (smaller number, larger number).
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2])
    (2.0, 2.2)
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0])
    (2.0, 2.0)
    """
    min_difference = None
    closest_elements = None
    for first_idx, first in enumerate(numbers):
        for second_idx, second in enumerate(numbers):
            if first_idx!= second_idx:
                current_difference = abs(first - second)
                if min_difference is None or current_difference < min_difference:
                    closest_elements = (first, second)
                    min_difference = current_difference
    return closest_elements

