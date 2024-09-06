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
    min_index = 0
    second_min_index = 1
    for i in range(0, len(numbers)):
        for j in range(i + 1, len(numbers)):
            if min_distance is None or abs(numbers[i] - numbers[j]) < min_distance:
                min_distance = abs(numbers[i] - numbers[j])
                min_index = i
                second_min_index = j
    return min(numbers[min_index], numbers[second_min_index]), max(numbers[min_index], numbers[second_min_index])

