from typing import List, Tuple


def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    """ From a supplied list of numbers (of length at least two) select and return two that are the closest to each
    other and return them in order (smaller number, larger number).
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2])
    (2.0, 2.2)
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0])
    (2.0, 2.0)
    """
    closest_number_1 = None
    closest_number_2 = None
    closest_distance = float('inf')
    for i in range(0, len(numbers)):
        for j in range(i + 1, len(numbers)):
            if abs(numbers[i] - numbers[j]) < closest_distance:
                closest_distance = abs(numbers[i] - numbers[j])
                closest_number_1 = numbers[i]
                closest_number_2 = numbers[j]
    return closest_number_1, closest_number_2

