from typing import List, Tuple


def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    """ From a supplied list of numbers (of length at least two) select and return two that are the closest to each
    other and return them in order (smaller number, larger number).
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2])
    (2.0, 2.2)
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0])
    (2.0, 2.0)
    """
    min_diff = float('inf')
    best_pair = (None, None)
    prev = numbers[0]
    for curr in numbers[1:]:
        diff = abs(curr - prev)
        if diff < min_diff:
            best_pair = (min(prev, curr), max(prev, curr))
            min_diff = diff
        prev = curr
    return best_pair

