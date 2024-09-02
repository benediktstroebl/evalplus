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
        return None, None
    numbers = sorted(numbers)
    index = 0
    closest = numbers[index]
    second_closest = numbers[index + 1]
    distance = abs(closest - second_closest)
    for i in range(1, len(numbers) - 1):
        current_distance = abs(numbers[i] - numbers[i + 1])
        if current_distance < distance:
            closest = numbers[i]
            second_closest = numbers[i + 1]
            distance = current_distance
    return closest, second_closest

