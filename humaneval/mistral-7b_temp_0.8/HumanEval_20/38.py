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
        raise ValueError("List should have more than one element")

    min_distance = min(abs(numbers[i] - numbers[i + 1]) for i in range(len(numbers) - 1))
    if len(numbers) > 2:
        max_distance = max(abs(numbers[i] - numbers[i + 1]) for i in range(len(numbers) - 1))
    else:
        max_distance = 0

    if min_distance == max_distance:
        return numbers[0], numbers[-1]
    elif min_distance > max_distance:
        return numbers[1], numbers[0]
    else:
        return numbers[0], numbers[1]
