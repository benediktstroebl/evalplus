from typing import List, Tuple


def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    """ From a supplied list of numbers (of length at least two) select and return two that are the closest to each
    other and return them in order (smaller number, larger number).
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2])
    (2.0, 2.2)
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0])
    (2.0, 2.0)
    """
    closest_numbers = sorted(numbers)
    closest_delta = abs(closest_numbers[0] - closest_numbers[1])
    numbers.remove(closest_numbers[0])
    numbers.remove(closest_numbers[1])
    for i in range(2, len(numbers)):
        delta = abs(numbers[i] - closest_numbers[0])
        if delta < closest_delta:
            closest_delta = delta
            closest_numbers[0], closest_numbers[1] = closest_numbers[1], closest_numbers[0]
    return closest_numbers[0], closest_numbers[1]

