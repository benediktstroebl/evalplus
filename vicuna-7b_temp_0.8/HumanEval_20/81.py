from typing import List, Tuple


def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    """ From a supplied list of numbers (of length at least two) select and return two that are the closest to each
    other and return them in order (smaller number, larger number).
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2])
    (2.0, 2.2)
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0])
    (2.0, 2.0)
    """
    closest_left, closest_right = float("inf"), float("-inf")
    left = float("inf")
    right = float("-inf")
    smallest = float("inf")
    smallest_diff = float("inf")
    i = 0
    for num in numbers:
        if num < smallest:
            smallest = num
            smallest_diff = smallest - left
        elif num > closest_right:
            closest_right = num
            right = smallest_diff
        elif num > smallest_diff and num < closest_left:
            closest_left = num
            left = smallest_diff
    return smallest, closest_left

