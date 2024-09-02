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
    closest_numbers = sorted_numbers[:2]
    smallest_distance = abs(closest_numbers[0] - closest_numbers[1])
    for i in range(2, len(sorted_numbers)):
        distance = abs(sorted_numbers[i] - closest_numbers[0])
        if distance < smallest_distance:
            smallest_distance = distance
            closest_numbers = sorted_numbers[i - 1:i + 1]
    return closest_numbers[0], closest_numbers[-1]

