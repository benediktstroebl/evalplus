from typing import List, Tuple


def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    """ From a supplied list of numbers (of length at least two) select and return two that are the closest to each
    other and return them in order (smaller number, larger number).
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2])
    (2.0, 2.2)
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0])
    (2.0, 2.0)
    """
    min_dist = float('inf')
    min_dist_index = -1
    min_dist_numbers = numbers[:]

    for i, number in enumerate(numbers):
        for j in range(i, len(numbers)):
            dist = abs(number - numbers[j])
            if dist < min_dist:
                min_dist = dist
                min_dist_index = j
                min_dist_numbers[:] = numbers[:j] + [numbers[j + 1]]

    return min_dist, min_dist_index

