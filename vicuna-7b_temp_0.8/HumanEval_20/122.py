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
        return None
    distance = [float("inf")] * len(numbers)
    for i, number in enumerate(numbers):
        for j in range(i + 1, len(numbers)):
            difference = abs(numbers[i] - numbers[j])
            if difference < distance[i]:
                distance[i] = difference
    return numbers[distance.index(min(distance))], numbers[distance.index(max(distance))]

