from typing import List, Tuple


def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    """ From a supplied list of numbers (of length at least two) select and return two that are the closest to each
    other and return them in order (smaller number, larger number).
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2])
    (2.0, 2.2)
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0])
    (2.0, 2.0)
    """
    assert len(numbers) >= 2
    min_distance = 100.0
    min_index = -1
    for i, number in enumerate(numbers):
        distance = abs(number - min_distance)
        if distance < min_distance:
            min_distance = distance
            min_index = i
    return numbers[min_index], numbers[(min_index + 1) % len(numbers
