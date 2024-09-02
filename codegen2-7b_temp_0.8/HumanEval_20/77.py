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
        raise ValueError("find_closest_elements requires at least two numbers")
    closest = numbers[0]
    min_dist = abs(closest - numbers[1])
    for i in range(len(numbers) - 1):
        dist = abs(closest - numbers[i + 1])
        if dist < min_dist:
            closest = numbers[i + 1]
            min_dist = dist
    return closest, closest

