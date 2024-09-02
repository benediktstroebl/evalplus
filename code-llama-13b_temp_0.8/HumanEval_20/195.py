from typing import List, Tuple


def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    """ From a supplied list of numbers (of length at least two) select and return two that are the closest to each
    other and return them in order (smaller number, larger number).
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2])
    (2.0, 2.2)
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0])
    (2.0, 2.0)
    """
    distance = abs(numbers[0] - numbers[1])
    first, second = numbers[0], numbers[1]
    for index in range(len(numbers) - 1):
        current_distance = abs(numbers[index] - numbers[index + 1])
        if current_distance < distance:
            distance = current_distance
            first, second = numbers[index], numbers[index + 1]
    return first, second

