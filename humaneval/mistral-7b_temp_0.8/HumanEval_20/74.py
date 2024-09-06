from typing import List, Tuple


def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    """ From a supplied list of numbers (of length at least two) select and return two that are the closest to each
    other and return them in order (smaller number, larger number).
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2])
    (2.0, 2.2)
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0])
    (2.0, 2.0)
    """
    number_set = set(numbers)
    first, second = None, None
    closest_pair_dist = float("inf")
    for number in number_set:
        if first is None:
            first = number
        else:
            second = number
            if abs(first - second) < closest_pair_dist:
                closest_pair_dist = abs(first - second)
    return sorted([first, second])
