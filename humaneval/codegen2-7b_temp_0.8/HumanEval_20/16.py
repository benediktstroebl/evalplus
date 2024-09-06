from typing import List, Tuple


def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    """ From a supplied list of numbers (of length at least two) select and return two that are the closest to each
    other and return them in order (smaller number, larger number).
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2])
    (2.0, 2.2)
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0])
    (2.0, 2.0)
    """
    if len(numbers) < 2:
        return None
    index_first = 0
    index_second = 1
    min_distance = None
    for index in range(1, len(numbers)):
        distance = abs(numbers[index] - numbers[index_first]) + abs(numbers[index] - numbers[index_second])
        if min_distance is None or min_distance > distance:
            min_distance = distance
            index_second = index_first
            index_first = index
    return numbers[index_first], numbers[index_
