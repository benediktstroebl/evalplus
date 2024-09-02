from typing import List, Tuple


def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    """ From a supplied list of numbers (of length at least two) select and return two that are the closest to each
    other and return them in order (smaller number, larger number).
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2])
    (2.0, 2.2)
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0])
    (2.0, 2.0)
    """
    numbers.sort()
    closest_tuple = (numbers[0], numbers[1])
    for x in range(len(numbers) - 1):
        if abs(numbers[x] - numbers[x + 1]) < abs(closest_tuple[0] - closest_tuple[1]):
            closest_tuple = (numbers[x], numbers[x + 1])
    return closest_tuple

