from typing import List, Tuple


def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    """ From a supplied list of numbers (of length at least two) select and return two that are the closest to each
    other and return them in order (smaller number, larger number).
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2])
    (2.0, 2.2)
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0])
    (2.0, 2.0)
    """
    numbers = sorted(numbers)
    closest_numbers = numbers[:2]
    closest_diff = abs(numbers[0] - numbers[1])
    closest_numbers = [n for n in closest_numbers if abs(n - numbers[0]) < closest_diff]
    closest_numbers = [n for n in closest_numbers if abs(n - numbers[1]) < closest_diff]
    return (closest_numbers[0], closest_numbers[1
