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
        raise ValueError("Can't select two closest from a list of less than two numbers.")
    min_distance = 10000000
    for i in range(0, len(numbers) - 1):
        for j in range(i + 1, len(numbers)):
            if abs(numbers[j] - numbers[i]) < min_distance:
                min_distance = abs(numbers[j] - numbers[i])
                current_closest = numbers[i], numbers[j]
    return current_closest

