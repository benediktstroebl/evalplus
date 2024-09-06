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
        raise ValueError("The input list of numbers should have at least two elements.")

    min_dist_index = 0
    min_dist_number = numbers[min_dist_index]
    min_dist = numbers[min_dist_index]

    for index in range(1, len(numbers)):
        curr_dist_number = numbers[index]
        curr_dist = index - min_dist_index
        if abs(curr_dist) < abs(min_dist):
            min_dist = curr_dist
            min_dist_index = index

    return min_dist, min_dist_index

