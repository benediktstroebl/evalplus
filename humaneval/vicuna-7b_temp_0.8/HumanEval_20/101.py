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
        return numbers[0], numbers[0]
    
    smallest_diff = float('inf')
    smallest_diff_index = 0
    largest_diff_index = 0
    smallest_number = numbers[0]
    largest_number = numbers[0]
    
    for i, value in enumerate(numbers):
        diff = value - smallest_number
        if diff < smallest_diff:
            smallest_diff = diff
            smallest_diff_index = i
    
    for i, value in enumerate(numbers):
        diff = value - largest_number
        if diff < largest_diff:
            largest_diff = diff
            largest_diff_index = i
    
    return smallest_number, largest_number