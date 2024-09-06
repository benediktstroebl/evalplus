from typing import List, Tuple


def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    """ From a supplied list of numbers (of length at least two) select and return two that are the closest to each
    other and return them in order (smaller number, larger number).
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2])
    (2.0, 2.2)
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0])
    (2.0, 2.0)
    """
    numbers = sorted(list(numbers))
    min_value = numbers[0]
    max_value = numbers[-1]
    min_diff = float("inf")
    for i in range(len(numbers)):
        if i != len(numbers) - 1:
            if abs(numbers[i] - numbers[i + 1]) < min_diff:
                min_diff = abs(numbers[i] - numbers[i + 1])
                min_value = min(numbers[i], numbers[i + 1])
                max_value = max(numbers[i], numbers[i + 1])
    return min_value, max_value

