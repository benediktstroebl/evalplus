from typing import List, Tuple


def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    """ From a supplied list of numbers (of length at least two) select and return two that are the closest to each
    other and return them in order (smaller number, larger number).
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2])
    (2.0, 2.2)
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0])
    (2.0, 2.0)
    """
    num_len = len(numbers)
    if num_len < 2:
        return numbers[0], numbers[0]

    min_dist = float("inf")
    min_value, min_idx = numbers[0], 0
    for i in range(1, num_len):
        dist = abs(numbers[i] - min_value)
        if dist < min_dist:
            min_dist = dist
            min_value = numbers[i]
            min_idx = i

    return min_value, numbers[min_id
