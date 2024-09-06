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
        return 0, 0
    
    smallest = max(numbers)
    biggest = min(numbers)
    middle = numbers[n//2]
    
    closest_to_smallest = smallest - (numbers[0] - smallest)
    closest_to_biggest = biggest - (numbers[-1] - biggest)
    
    return closest_to_smallest, closest_to_biggest

