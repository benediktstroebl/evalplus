from typing import List, Tuple


def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    """ From a supplied list of numbers (of length at least two) select and return two that are the closest to each
    other and return them in order (smaller number, larger number).
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2])
    (2.0, 2.2)
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0])
    (2.0, 2.0)
    """
    numbers_sorted = sorted(numbers)
    smallest = numbers_sorted[0]
    largest = numbers_sorted[-1]
    if len(numbers) == 2:
        return smallest, largest
    for i in range(1, len(numbers)):
        if abs(numbers_sorted[i] - numbers_sorted[i - 1]) < abs(numbers_sorted[0] - numbers_sorted[1]):
            smallest, largest = numbers_sorted[i], numbers_sorted[i - 1]
    return smallest, largest
