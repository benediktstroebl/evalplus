from typing import List, Tuple


def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    """ From a supplied list of numbers (of length at least two) select and return two that are the closest to each
    other and return them in order (smaller number, larger number).
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2])
    (2.0, 2.2)
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0])
    (2.0, 2.0)
    """
    current_min_value: float = numbers[0]
    current_min_index: int = 0
    for index in range(1, len(numbers)):
        value: float = numbers[index]
        if value < current_min_value:
            current_min_value = value
            current_min_index = index
    return numbers[current_min_index], numbers[current_min_index
