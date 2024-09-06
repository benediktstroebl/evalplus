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

    closest_pairs = []

    for i in range(n - 1):
        for j in range(i + 1, n):
            diff = abs(numbers[i] - numbers[j])
            if diff < float("inf"):
                closest_pairs.append((numbers[i], numbers[j]))

    if len(closest_pairs) == 0:
        return None

    min_diff = min(closest_pairs, key=lambda x: x[1] - x[0])
    return min_diff[0], min_diff[1]
