from typing import List, Tuple


def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    """ From a supplied list of numbers (of length at least two) select and return two that are the closest to each
    other and return them in order (smaller number, larger number).
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2])
    (2.0, 2.2)
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0])
    (2.0, 2.0)
    """
    sorted_nums = sorted(numbers)
    smallest, second_smallest = sorted_nums[0], sorted_nums[1]
    closest = smallest
    n = len(numbers)
    for i in range(2, n):
        if abs(smallest - numbers[i]) < abs(second_smallest - numbers[i]):
            second_smallest = smallest
            smallest = numbers[i]
        elif abs(second_smallest - numbers[i]) < abs(smallest - numbers[i]):
            second_smallest = numbers[i]
    return smallest, second_smallest

