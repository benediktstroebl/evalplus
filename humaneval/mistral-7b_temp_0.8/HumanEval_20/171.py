from typing import List, Tuple


def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    """ From a supplied list of numbers (of length at least two) select and return two that are the closest to each
    other and return them in order (smaller number, larger number).
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2])
    (2.0, 2.2)
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0])
    (2.0, 2.0)
    """
    min_diff = abs(numbers[0] - numbers[1])
    min_diff_numbers = numbers[:2]
    for i in range(2, len(numbers)):
        if abs(numbers[i] - numbers[0]) < min_diff:
            min_diff = abs(numbers[i] - numbers[0])
            min_diff_numbers = [numbers[i], numbers[0]]
        if abs(numbers[i] - numbers[1]) < min_diff:
            min_diff = abs(numbers[i] - numbers[1])
            min_diff_numbers = [numbers[1], numbers[i]]
    return min_diff_numbers
