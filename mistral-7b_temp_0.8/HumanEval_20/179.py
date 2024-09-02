from typing import List, Tuple


def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    """ From a supplied list of numbers (of length at least two) select and return two that are the closest to each
    other and return them in order (smaller number, larger number).
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2])
    (2.0, 2.2)
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0])
    (2.0, 2.0)
    """
    smallest = 0
    for i, num in enumerate(numbers):
        if i == 0:
            continue
        else:
            if abs(numbers[i] - numbers[smallest]) < abs(numbers[i] - numbers[i - 1]):
                smallest = i
    return numbers[smallest - 1], numbers[smallest]
