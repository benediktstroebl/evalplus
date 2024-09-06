from typing import List, Tuple


def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    """ From a supplied list of numbers (of length at least two) select and return two that are the closest to each
    other and return them in order (smaller number, larger number).
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2])
    (2.0, 2.2)
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0])
    (2.0, 2.0)
    """
    min_diff = float('inf')
    max_diff = float('-inf')
    smallest_number = numbers[0]
    largest_number = numbers[-1]
    
    for i in range(1, len(numbers)):
        smallest_number = min(smallest_number, numbers[i])
        largest_number = max(largest_number, numbers[i])
        
        diff = abs(smallest_number - largest_number)
        if diff < min_diff:
            min_diff = diff
            closest_numbers = (smallest_number, largest_number)
        elif diff > max_diff:
            max_diff = diff
    
    return closest_numbers

