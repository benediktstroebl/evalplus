from typing import List, Tuple


def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    """ From a supplied list of numbers (of length at least two) select and return two that are the closest to each
    other and return them in order (smaller number, larger number).
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2])
    (2.0, 2.2)
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0])
    (2.0, 2.0)
    """
    # find the largest and the smallest
    if len(numbers) < 2:
        raise ValueError("at least 2 numbers required")
    largest = max(numbers)
    smallest = min(numbers)
    # find the closest to the largest
    closest_larger_than_largest = sorted(numbers, key=lambda x: abs(x - largest), reverse=True)[1]
    # find the closest to the smallest
    closest_smaller_than_smallest = sorted(numbers, key=lambda x: abs(x - smallest))[0]
    return closest_larger_than_largest, closest_smaller_than_smallest
