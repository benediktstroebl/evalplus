from typing import List, Tuple


def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    """ From a supplied list of numbers (of length at least two) select and return two that are the closest to each
    other and return them in order (smaller number, larger number).
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2])
    (2.0, 2.2)
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0])
    (2.0, 2.0)
    """
    min_diff = float("inf")
    numbers = sorted(numbers)
    for index, _ in enumerate(numbers):
        start = 0 if index == 0 else index - 1
        end = index + 1 if index != len(numbers) - 1 else len(numbers)
        for idx in range(start, end):
            current_diff = abs(numbers[index] - numbers[idx])
            if current_diff <= min_diff:
                min_diff = current_diff
                closest_elements = (numbers[index], numbers[idx])

    return closest_elements


import unittest
