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
        raise ValueError('Length must be at least 2')

    closest_numbers: List[float] = [numbers[0], numbers[1]]
    for i in range(2, len(numbers)):
        if abs(closest_numbers[0] - closest_numbers[1]) > abs(numbers[i] - closest_numbers[0]):
            closest_numbers[1] = closest_numbers[0]
            closest_numbers[0] = numbers[i]
        elif abs(closest_numbers[0] - closest_numbers[1]) > abs(numbers[i] - closest_numbers[1]):
            closest_numbers[1] = numbers[i]
        else:
            pass

    return closest_numbers

