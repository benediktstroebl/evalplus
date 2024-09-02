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
        raise ValueError("The input list must have at least two elements")
    
    min_dist = float('inf')
    min_diff = float('inf')
    closest_pairs = []
    
    for i, j in combinations(range(len(numbers)), 2):
        a = numbers[i]
        b = numbers[j]
        dist = abs(a - b)
        
        if dist < min_dist:
            min_dist = dist
            min_diff = abs(a - b)
            closest_pairs.append((i, j))
    
    if closest_pairs:
        return min_diff, min_dist
    else:
        return float('inf'), float('inf')

