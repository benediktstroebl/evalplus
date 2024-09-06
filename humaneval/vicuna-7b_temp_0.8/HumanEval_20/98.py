from typing import List, Tuple


def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    """ From a supplied list of numbers (of length at least two) select and return two that are the closest to each
    other and return them in order (smaller number, larger number).
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2])
    (2.0, 2.2)
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0])
    (2.0, 2.0)
    """
    smallest_distance = float('inf')
    smallest_distance_index = -1
    for i in range(1, len(numbers)):
        for j in range(i):
            distance = abs(numbers[i] - numbers[j])
            if distance < smallest_distance:
                smallest_distance = distance
                smallest_distance_index = i
    return numbers[smallest_distance_index], numbers[smallest_distance + 1]

