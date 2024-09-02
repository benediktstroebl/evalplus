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
    index = 1
    smallest_distance = sorted_numbers[index] - sorted_numbers[0]
    for i in range(1, len(sorted_numbers)):
        current_distance = sorted_numbers[i] - sorted_numbers[i - 1]
        if current_distance < smallest_distance:
            index = i
            smallest_distance = current_distance
    return sorted_numbers[index - 1], sorted_numbers[index
