from typing import List, Tuple


def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    """ From a supplied list of numbers (of length at least two) select and return two that are the closest to each
    other and return them in order (smaller number, larger number).
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2])
    (2.0, 2.2)
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0])
    (2.0, 2.0)
    """
    numbers.sort()
    min_distance = 100
    smallest_pair = (0, 0)
    for i in range(1, len(numbers)):
        if abs(numbers[i] - numbers[i - 1]) < min_distance:
            min_distance = abs(numbers[i] - numbers[i - 1])
            smallest_pair = (numbers[i - 1], numbers[i])
    return smallest_pair[0], smallest_pair[1]

