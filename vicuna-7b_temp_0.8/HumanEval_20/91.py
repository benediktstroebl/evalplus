from typing import List, Tuple


def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    """ From a supplied list of numbers (of length at least two) select and return two that are the closest to each
    other and return them in order (smaller number, larger number).
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2])
    (2.0, 2.2)
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0])
    (2.0, 2.0)
    """
    min_distance = float('inf')
    min_index_a, min_index_b = 0, 0
    
    for i in range(1, len(numbers)):
        index_a = (numbers[i] - numbers[min_index_a]).dot(numbers[min_index_a] - numbers[min_index_b])
        index_b = (numbers[min_index_b] - numbers[i]).dot(numbers[min_index_b] - numbers[min_index_a])
        
        distance_a = index_a ** 2
        distance_b = index_b ** 2
        
        if distance_a < min_distance:
            min_distance = distance_a
            min_index_a, min_index_b = i, min_index_b
        
    return numbers[min_index_a], numbers[min_index_b]