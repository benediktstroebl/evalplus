from typing import List, Tuple


def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    """ From a supplied list of numbers (of length at least two) select and return two that are the closest to each
    other and return them in order (smaller number, larger number).
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2])
    (2.0, 2.2)
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0])
    (2.0, 2.0)
    """
    if len(numbers) <= 1:
        raise ValueError("list length must be at least two")
    min_dist = 100000000000000
    closest_numbers: Tuple[float, float] = (0, 0)
    for i in range(0, len(numbers)):
        for j in range(0, len(numbers)):
            if i == j:
                continue
            diff = abs(numbers[i] - numbers[j])
            if diff < min_dist:
                min_dist = diff
                closest_numbers = (numbers[i], numbers[j])
    return closest_numbers
