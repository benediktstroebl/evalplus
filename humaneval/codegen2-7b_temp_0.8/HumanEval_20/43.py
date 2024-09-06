from typing import List, Tuple


def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    """ From a supplied list of numbers (of length at least two) select and return two that are the closest to each
    other and return them in order (smaller number, larger number).
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2])
    (2.0, 2.2)
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0])
    (2.0, 2.0)
    """
    closest_left = min(numbers)
    closest_right = max(numbers)
    for i in range(len(numbers) - 1):
        current_left = numbers[i]
        current_right = numbers[i + 1]
        if current_left < closest_left < current_right:
            closest_left = current_left
        elif current_right < closest_right < current_left:
            closest_right = current_right
    return closest_left, closest_right

