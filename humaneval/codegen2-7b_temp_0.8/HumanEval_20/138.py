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
        return None, None
    closest_numbers = [numbers[0]]
    for number in numbers[1:]:
        if abs(number - closest_numbers[0]) > abs(number - closest_numbers[-1]):
            closest_numbers.pop()
        closest_numbers.append(number)
    return closest_numbers[0], closest_numbers[-1]

