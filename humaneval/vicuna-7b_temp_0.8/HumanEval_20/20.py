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
    min_index = 0
    min_number = numbers[0]
    
    for i in range(1, len(numbers)):
        for j in range(i, len(numbers)):
            distance = (numbers[i] - numbers[j]) ** 2
            if distance < min_distance:
                min_index = j
                min_distance = distance
                min_number = numbers[j]
    
    return min_number, min_index

