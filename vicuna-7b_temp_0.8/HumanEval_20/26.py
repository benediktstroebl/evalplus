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
        return numbers, numbers[0]
    min_dist = float('inf')
    min_index = 0
    for i in range(1, len(numbers)):
        curr_dist = numbers[i] - numbers[min_index]
        curr_index = min(i, len(numbers) - 1)
        dist_plus_index = curr_index - min_index
        dist = dist_plus_index * (curr_dist + 1)
        if dist < min_dist:
            min_dist = dist
            min_index = curr_index
    return numbers[min_index], numbers[min_index + 1]

