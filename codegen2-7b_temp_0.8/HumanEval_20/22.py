from typing import List, Tuple


def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    """ From a supplied list of numbers (of length at least two) select and return two that are the closest to each
    other and return them in order (smaller number, larger number).
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2])
    (2.0, 2.2)
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0])
    (2.0, 2.0)
    """
    smallest_diff = numbers[0]
    smallest_index = 0
    for i, num in enumerate(numbers):
        diff = abs(num - smallest_diff)
        if diff > 0:
            smallest_diff = num
            smallest_index = i
    return numbers[smallest_index], numbers[(smallest_index + 1) % len(numbers)]

