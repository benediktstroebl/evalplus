from typing import List, Tuple


def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    """ From a supplied list of numbers (of length at least two) select and return two that are the closest to each
    other and return them in order (smaller number, larger number).
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2])
    (2.0, 2.2)
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0])
    (2.0, 2.0)
    """

    min_1 = float("inf")
    min_2 = float("inf")
    max_1 = float("-inf")
    max_2 = float("-inf")
    for i in numbers:
        if i > max_1:
            max_2 = max_1
            max_1 = i
        elif i > max_2:
            max_2 = i
        if i < min_1:
            min_2 = min_1
            min_1 = i
        elif i < min_2:
            min_2 = i
    return (min_1, min_2) if min_1 < min_2 else (min_2, min_1)
