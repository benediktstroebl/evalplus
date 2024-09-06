from typing import List, Tuple


def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    """ From a supplied list of numbers (of length at least two) select and return two that are the closest to each
    other and return them in order (smaller number, larger number).
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2])
    (2.0, 2.2)
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0])
    (2.0, 2.0)
    """
    numbers = sorted(numbers)
    min_distance = numbers[1] - numbers[0]
    min_distance_i = 0
    for i in range(len(numbers) - 1):
        if numbers[i + 1] - numbers[i] < min_distance:
            min_distance = numbers[i + 1] - numbers[i]
            min_distance_i = i
    return numbers[min_distance_i], numbers[min_distance_i + 1]

