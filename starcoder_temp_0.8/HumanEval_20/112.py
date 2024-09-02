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
    first_closest_idx = sorted_numbers.index(sorted_numbers[1])
    second_closest_idx = sorted_numbers.index(sorted_numbers[2])
    if first_closest_idx > second_closest_idx:
        return sorted_numbers[second_closest_idx], sorted_numbers[first_closest_idx]
    else:
        return sorted_numbers[first_closest_idx], sorted_numbers[second_closest_idx]
