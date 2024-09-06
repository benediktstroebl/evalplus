from typing import List, Tuple


def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    """ From a supplied list of numbers (of length at least two) select and return two that are the closest to each
    other and return them in order (smaller number, larger number).
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2])
    (2.0, 2.2)
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0])
    (2.0, 2.0)
    """
    closest = abs(numbers[0] - numbers[1])
    closest_pair = (numbers[0], numbers[1])
    i = 0
    while i + 1 < len(numbers):
        pair_diff = abs(numbers[i] - numbers[i + 1])
        if pair_diff < closest:
            closest = pair_diff
            closest_pair = (numbers[i], numbers[i + 1])
        i += 1
    return closest_pair

