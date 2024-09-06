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
    i = 0
    min_dist = float("inf")
    min_1 = numbers[0]
    min_2 = numbers[1]
    while i < len(numbers) - 1:
        if abs(numbers[i] - numbers[i + 1]) < min_dist:
            min_dist = abs(numbers[i] - numbers[i + 1])
            min_1 = numbers[i]
            min_2 = numbers[i + 1]
        i += 1
    return min_1, min_2

