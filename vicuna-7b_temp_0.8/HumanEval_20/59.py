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
        return (0.0, 0.0)
    
    smallest = numbers[0]
    closest = numbers[0]
    
    for num in numbers[1:]:
        distance_from_smallest = abs(num - smallest)
        distance_from_closest = abs(num - closest)
        
        if distance_from_smallest < distance_from_closest:
            smallest, closest = num, closest
        
    return (smallest, closest)

