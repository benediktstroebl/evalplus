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
    min_diff = 10000000
    i = 0
    j = 0
    while i < len(sorted_numbers):
        for k in range(i + 1, len(sorted_numbers)):
            diff = sorted_numbers[k] - sorted_numbers[i]
            if diff < min_diff:
                min_diff = diff
                j = k
        i += 1
    return sorted_numbers[j], sorted_numbers[i]

