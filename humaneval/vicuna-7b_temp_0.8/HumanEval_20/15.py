from typing import List, Tuple


def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    """ From a supplied list of numbers (of length at least two) select and return two that are the closest to each
    other and return them in order (smaller number, larger number).
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2])
    (2.0, 2.2)
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0])
    (2.0, 2.0)
    """
    n = len(numbers)
    if n < 2:
        return tuple()
    
    smallest_distance = float('inf')
    smallest_number = None
    closest_number = numbers[0]
    for number in numbers[1:]:
        distance = number - closest_number
        if distance < smallest_distance:
            smallest_distance = distance
            smallest_number = number
    
    return closest_number, smallest_number

