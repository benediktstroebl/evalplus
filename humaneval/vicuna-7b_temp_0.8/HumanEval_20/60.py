from typing import List, Tuple


def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    """ From a supplied list of numbers (of length at least two) select and return two that are the closest to each
    other and return them in order (smaller number, larger number).
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2])
    (2.0, 2.2)
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0])
    (2.0, 2.0)
    """
    min_distance = float('inf')
    smallest_distance = float('inf')
    smallest_distance_number = float('inf')
    smallest_distance_index = -1

    for number in numbers:
        distance = abs(number - smallest_distance_number)

        if distance < min_distance:
            min_distance = distance
            smallest_distance = smallest_distance_number
            smallest_distance_index = numbers.index(smallest_distance_number)

    return smallest_distance, smallest_distance_index

