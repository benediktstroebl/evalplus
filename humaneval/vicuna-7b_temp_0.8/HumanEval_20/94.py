from typing import List, Tuple


def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    """ From a supplied list of numbers (of length at least two) select and return two that are the closest to each
    other and return them in order (smaller number, larger number).
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2])
    (2.0, 2.2)
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0])
    (2.0, 2.0)
    """
    closest_start = 0
    closest_end = 1
    closest_diff = numbers[closest_start] - numbers[closest_end]
    for i in range(1, len(numbers)):
        for j in range(i+1, len(numbers)):
            current_start = j
            current_diff = numbers[j] - numbers[i]
            if abs(current_diff) < abs(closest_diff):
                closest_start = i
                closest_end = j
                closest_diff = current_diff
    return closest_start, closest_end

