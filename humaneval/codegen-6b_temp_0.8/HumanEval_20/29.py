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
    closest_to_first = numbers[0]
    closest_to_second = numbers[1]
    if abs(closest_to_first - closest_to_second) < abs(closest_to_second - (closest_to_first + closest_to_second) / 2):
        return closest_to_first, closest_to_second
    else:
        return closest_to_second, closest_to_first

