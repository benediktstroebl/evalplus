from typing import List, Tuple


def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    """ From a supplied list of numbers (of length at least two) select and return two that are the closest to each
    other and return them in order (smaller number, larger number).
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2])
    (2.0, 2.2)
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0])
    (2.0, 2.0)
    """
    i = 0
    min_distance = float('inf')
    for i in range(len(numbers) - 1):
        distance = abs(numbers[i] - numbers[i + 1])
        if distance < min_distance:
            min_distance = distance
            first_num = min(numbers[i], numbers[i + 1])
            second_num = max(numbers[i], numbers[i + 1])
    return first_num, second_num

