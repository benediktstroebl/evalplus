from typing import List, Tuple


def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    """ From a supplied list of numbers (of length at least two) select and return two that are the closest to each
    other and return them in order (smaller number, larger number).
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2])
    (2.0, 2.2)
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0])
    (2.0, 2.0)
    """
    if len(numbers) < 2:
        raise ValueError("Number of elements in list must be at least 2")

    closest = numbers[1] - numbers[0]
    closest_left, closest_right = numbers[0], numbers[1]
    for i in range(2, len(numbers)):
        delta = numbers[i] - numbers[i-1]
        if delta < closest:
            closest = delta
            closest_left = numbers[i-1]
            closest_right = numbers[i]
    return closest_left, closest_right
