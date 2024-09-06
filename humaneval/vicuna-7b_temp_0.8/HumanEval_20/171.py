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
        return 0, 0
    min_distance = 1000000000
    min_index = 0
    for i in range(1, len(numbers)):
        distance = (numbers[i] - numbers[min_index]) ** 2
        if distance < min_distance:
            min_distance = distance
            min_index = i
    return numbers[min_index], numbers[min_index + 1]

