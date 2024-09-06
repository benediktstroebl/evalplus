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
        return None

    min_dist = float("inf")
    min_dist_index = -1
    for i in range(n):
        for j in range(i + 1, n):
            dx = numbers[j] - numbers[i]
            dy = numbers[i + 1] - numbers[i]
            dist_sqr = dx ** 2 + dy ** 2
            dist_sqr = max(dist_sqr, min_dist_sqr)
            min_dist = min(min_dist, dist_sqr)
            min_dist_index = i

    if min_dist < 1.0:
        return numbers[min_dist_index], numbers[min_dist_index + 1]
    else:
        return None

