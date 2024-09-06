from typing import List, Tuple


def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    """ From a supplied list of numbers (of length at least two) select and return two that are the closest to each
    other and return them in order (smaller number, larger number).
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2])
    (2.0, 2.2)
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0])
    (2.0, 2.0)
    """
    numbers_ = sorted(numbers)
    min_diff = abs(numbers_[0] - numbers_[1])
    best_pair = tuple(sorted([numbers_[0], numbers_[1]]))
    for index in range(1, len(numbers_) - 1):
        diff = abs(numbers_[index] - numbers_[index + 1])
        if diff < min_diff:
            best_pair = tuple(sorted([numbers_[index], numbers_[index + 1]]))
            min_diff = diff
    return best_pair

