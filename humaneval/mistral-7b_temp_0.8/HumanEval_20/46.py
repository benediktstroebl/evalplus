from typing import List, Tuple


def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    """ From a supplied list of numbers (of length at least two) select and return two that are the closest to each
    other and return them in order (smaller number, larger number).
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2])
    (2.0, 2.2)
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0])
    (2.0, 2.0)
    """
    sorted_numbers = sorted(numbers)
    minimum_diff = float('inf')
    closest_to_minimum = None
    next_closest_to_minimum = None

    for i in range(len(sorted_numbers) - 1):
        diff = abs(sorted_numbers[i] - sorted_numbers[i + 1])
        if diff < minimum_diff:
            minimum_diff = diff
            closest_to_minimum = sorted_numbers[i]
            next_closest_to_minimum = sorted_numbers[i + 1]

    return closest_to_minimum, next_closest_to_minimum

