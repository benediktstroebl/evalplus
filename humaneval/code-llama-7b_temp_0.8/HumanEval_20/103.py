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
        raise ValueError

    smallest_diff = numbers[1] - numbers[0]
    closest_numbers = numbers[0], numbers[1]
    for i in range(2, len(numbers)):
        diff = numbers[i] - numbers[i - 1]
        if abs(diff) < smallest_diff:
            smallest_diff = abs(diff)
            closest_numbers = numbers[i - 1], numbers[i]
    return closest_numbers
