from typing import List, Tuple


def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    """ From a supplied list of numbers (of length at least two) select and return two that are the closest to each
    other and return them in order (smaller number, larger number).
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2])
    (2.0, 2.2)
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0])
    (2.0, 2.0)
    """
    smallest_diff = numbers[1] - numbers[0]
    min_number = numbers[0]
    max_number = numbers[1]
    for i in range(len(numbers)):
        for j in range(i + 1, len(numbers)):
            diff = numbers[j] - numbers[i]
            if diff < smallest_diff:
                smallest_diff = diff
                min_number = numbers[i]
                max_number = numbers[j]
    return min_number, max_number

