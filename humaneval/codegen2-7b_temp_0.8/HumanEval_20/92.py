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
        raise ValueError("Array must be at least 2 elements long")
    closest_numbers = (numbers[0], numbers[0])
    for num in numbers[1:]:
        if abs(num) < abs(closest_numbers[0]):
            closest_numbers = (num, closest_numbers[0])
        elif abs(num) > abs(closest_numbers[1]):
            closest_numbers = (closest_numbers[1], num)
    return closest_numbers
