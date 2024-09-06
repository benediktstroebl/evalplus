from typing import List, Tuple


def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    """ From a supplied list of numbers (of length at least two) select and return two that are the closest to each
    other and return them in order (smaller number, larger number).
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2])
    (2.0, 2.2)
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0])
    (2.0, 2.0)
    """
    if len(numbers) < 2:
        return None
    smallest = numbers[0]
    smallest_diff = abs(smallest)
    for num in numbers[1:]:
        num_diff = abs(num)
        if num_diff < smallest_diff:
            smallest_diff = num_diff
            smallest = num
    largest = smallest
    largest_diff = abs(largest)
    for num in numbers[1:]:
        num_diff = abs(num)
        if num_diff > largest_diff:
            largest_diff = num_diff
            largest = num
    return smallest, largest

