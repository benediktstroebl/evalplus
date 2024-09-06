from typing import List, Tuple


def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    """ From a supplied list of numbers (of length at least two) select and return two that are the closest to each
    other and return them in order (smaller number, larger number).
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2])
    (2.0, 2.2)
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0])
    (2.0, 2.0)
    """
    i = 0
    j = 1
    while j < len(numbers):
        if abs(numbers[j] - numbers[i]) < abs(numbers[j + 1] - numbers[i]):
            j += 1
        else:
            i += 1
            j = i + 1
    return numbers[i], numbers[j]

