from typing import List, Tuple


def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    """ From a supplied list of numbers (of length at least two) select and return two that are the closest to each
    other and return them in order (smaller number, larger number).
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2])
    (2.0, 2.2)
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0])
    (2.0, 2.0)
    """
    n = len(numbers)
    if n < 2:
        return (0, 0)
    best_dist = float('inf')
    closest_pair = None
    for i in range(1, n):
        for j in range(i + 1, n):
            dist = abs(numbers[i] - numbers[j])
            if dist < best_dist:
                best_dist = dist
                closest_pair = (i, j)
    return closest_pair

