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
        return tuple()
    
    smallest_diff = float("inf")
    closest_pair = None
    for i in range(len(numbers) - 1):
        curr_diff = numbers[i] - numbers[i + 1]
        if curr_diff < smallest_diff:
            smallest_diff = curr_diff
            closest_pair = (numbers[i], numbers[i + 1])
    
    return smallest_diff, closest_pair

