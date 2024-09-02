from typing import List, Tuple


def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    """ From a supplied list of numbers (of length at least two) select and return two that are the closest to each
    other and return them in order (smaller number, larger number).
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2])
    (2.0, 2.2)
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0])
    (2.0, 2.0)
    """
    if not numbers:
        raise ValueError("Input list cannot be empty.")

    if len(numbers) < 2:
        raise ValueError("Input list must have at least 2 elements.")

    sorted_numbers = sorted(numbers)
    idx = 0
    min_diff = abs(sorted_numbers[idx] - sorted_numbers[idx + 1])

    for x in range(len(sorted_numbers) - 1):
        new_diff = abs(sorted_numbers[x] - sorted_numbers[x + 1])

        if new_diff < min_diff:
            min_diff = new_diff
            idx = x

    return sorted_numbers[idx], sorted_numbers[idx + 1]

