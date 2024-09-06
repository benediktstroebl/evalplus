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
        return (float('inf'), float('-inf'))
    min_distance = float('inf')
    closest_numbers = (float('inf'), float('-inf'))
    for i in range(1, len(numbers)):
        for j in range(i):
            distance = (numbers[i] - numbers[j]) ** 2
            min_distance = min(min_distance, distance)
            if min_distance < 1.0:
                closest_numbers = (numbers[i], numbers[j])
                break
    return closest_numbers

