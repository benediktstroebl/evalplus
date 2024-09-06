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
    min_diff = abs(numbers[0] - numbers[1])
    min_numbers = (numbers[0], numbers[1])
    for a, b in zip(numbers[:-1], numbers[1:]):
        diff = abs(a - b)
        if diff < min_diff:
            min_diff = diff
            min_numbers = (a, b)
    return min_numbers

