from typing import List, Tuple


def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    """ From a supplied list of numbers (of length at least two) select and return two that are the closest to each
    other and return them in order (smaller number, larger number).
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2])
    (2.0, 2.2)
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0])
    (2.0, 2.0)
    """
    closest_numbers = [numbers[0], numbers[1]]
    for number in numbers[2:]:
        current_closest = [
            abs(number - closest_numbers[0]),
            abs(number - closest_numbers[1]),
        ]
        if current_closest[0] < current_closest[1]:
            closest_numbers = [number, closest_numbers[1]]
        else:
            closest_numbers = [closest_numbers[0], number]
    return closest_numbers[0], closest_numbers[
