from typing import List, Tuple


def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    """ From a supplied list of numbers (of length at least two) select and return two that are the closest to each
    other and return them in order (smaller number, larger number).
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2])
    (2.0, 2.2)
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0])
    (2.0, 2.0)
    """
    numbers.sort()
    best_dist = abs(numbers[0] - numbers[1])
    best_pair = (numbers[0], numbers[1])
    for i in range(len(numbers) - 1):
        dist = abs(numbers[i] - numbers[i + 1])
        if dist < best_dist:
            best_dist = dist
            best_pair = (numbers[i], numbers[i + 1])
    return best_pair

