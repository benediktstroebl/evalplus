from typing import List, Tuple


def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    """ From a supplied list of numbers (of length at least two) select and return two that are the closest to each
    other and return them in order (smaller number, larger number).
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2])
    (2.0, 2.2)
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0])
    (2.0, 2.0)
    """

    min_distance = None
    sorted_numbers = sorted(numbers)
    first_idx, second_idx = 0, 0
    for i in range(len(sorted_numbers) - 1):
        first_element = sorted_numbers[i]
        second_element = sorted_numbers[i + 1]
        difference = second_element - first_element
        if min_distance is None or abs(difference) < min_distance:
            min_distance = abs(difference)
            first_idx, second_idx = i, i + 1

    return sorted_numbers[first_idx], sorted_numbers[second_idx]
    
    
