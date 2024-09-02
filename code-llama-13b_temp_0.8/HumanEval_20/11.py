from typing import List, Tuple


def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    """ From a supplied list of numbers (of length at least two) select and return two that are the closest to each
    other and return them in order (smaller number, larger number).
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2])
    (2.0, 2.2)
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0])
    (2.0, 2.0)
    """
    numbers.sort()
    closest_tuple = (numbers[0], numbers[1])
    closest_distance = abs(closest_tuple[1] - closest_tuple[0])
    for i in range(0, len(numbers)):
        for j in range(i + 1, len(numbers)):
            new_distance = abs(numbers[j] - numbers[i])
            if new_distance < closest_distance:
                closest_tuple = (numbers[i], numbers[j])
                closest_distance = abs(closest_tuple[1] - closest_tuple[0])
    return closest_tuple

