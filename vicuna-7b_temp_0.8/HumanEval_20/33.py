from typing import List, Tuple


def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    """ From a supplied list of numbers (of length at least two) select and return two that are the closest to each
    other and return them in order (smaller number, larger number).
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2])
    (2.0, 2.2)
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0])
    (2.0, 2.0)
    """
    min_dist_to_self = [0] * len(numbers)
    min_dist_to_other = [float("inf")] * len(numbers)
    for i, num in enumerate(numbers):
        for j in range(i + 1, len(numbers)):
            d = abs(num - numbers[j])
            min_dist_to_self[i] = min(min_dist_to_self[i], d)
            min_dist_to_other[j] = min(min_dist_to_other[j], d)
    return min_dist_to_self[0], min_dist_to_other[-1]