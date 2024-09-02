from typing import List, Tuple


def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    """ From a supplied list of numbers (of length at least two) select and return two that are the closest to each
    other and return them in order (smaller number, larger number).
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2])
    (2.0, 2.2)
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0])
    (2.0, 2.0)
    """
    sorted_numbers = sorted(numbers)
    closest_pairs = []
    for i in range(len(sorted_numbers) - 1):
        closest_pairs.append((sorted_numbers[i], sorted_numbers[i + 1]))
    min_diff = float("inf")
    min_pair = None
    for pair in closest_pairs:
        diff = abs(pair[0] - pair[1])
        if diff < min_diff:
            min_diff = diff
            min_pair = pair
    return min_pair

