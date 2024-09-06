from typing import List, Tuple


def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    """ From a supplied list of numbers (of length at least two) select and return two that are the closest to each
    other and return them in order (smaller number, larger number).
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2])
    (2.0, 2.2)
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0])
    (2.0, 2.0)
    """
    closest_elements = numbers[0], numbers[1]
    for number in numbers[2:]:
        if abs(closest_elements[0] - closest_elements[1]) > abs(number - closest_elements[1]):
            closest_elements = closest_elements[1], number
        elif abs(closest_elements[0] - closest_elements[1]) > abs(number - closest_elements[0]):
            closest_elements = number, closest_elements[0]
    return closest_elements
