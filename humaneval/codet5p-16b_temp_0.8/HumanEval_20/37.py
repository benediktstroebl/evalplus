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
        raise ValueError('At least 2 elements required')
    min_diff = float('inf')
    first, second = 0, 1
    for i, n in enumerate(numbers[:-1]):
        for j in range(i + 1, len(numbers)):
            if abs(numbers[j] - numbers[i]) < min_diff:
                min_diff = abs(numbers[j] - numbers[i])
                first = i
                second = j
    return (numbers[first], numbers[second])
    
    
