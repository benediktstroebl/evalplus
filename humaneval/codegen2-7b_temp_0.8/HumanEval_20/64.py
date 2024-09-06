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
        raise ValueError("The list of numbers supplied should at least have 2 elements")
    smallest_distance = numbers[0]
    closest_numbers = [smallest_distance, smallest_distance]
    for number in numbers[1:]:
        if abs(number - smallest_distance) > abs(number - closest_numbers[1]):
            closest_numbers = [number, smallest_distance]
        else:
            closest_numbers = [smallest_distance, number]
            smallest_distance = number
    return tuple(closest_numbers
