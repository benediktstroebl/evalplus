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
    min_distance, second_closest = float('inf'), float('inf')
    for i in range(len(numbers)):
        for j in range(i + 1, len(numbers)):
            distance = numbers[i] - numbers[j]
            if abs(distance) < min_distance:
                second_closest = min_distance
                min_distance = distance
            elif abs(distance) < second_closest:
                second_closest = distance
    return (min_distance, second_closest)
