from typing import List, Tuple


def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    """ From a supplied list of numbers (of length at least two) select and return two that are the closest to each
    other and return them in order (smaller number, larger number).
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2])
    (2.0, 2.2)
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0])
    (2.0, 2.0)
    """
    if len(numbers) == 0:
        raise ValueError
    closest_numbers = [numbers[0], numbers[0]]
    for number in numbers[1:]:
        if abs(closest_numbers[0] - number) > abs(closest_numbers[1] - number):
            closest_numbers[0] = number
        else:
            closest_numbers[1] = number
    return closest_numbers

