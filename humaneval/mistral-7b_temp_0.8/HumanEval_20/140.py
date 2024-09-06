from typing import List, Tuple


def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    """ From a supplied list of numbers (of length at least two) select and return two that are the closest to each
    other and return them in order (smaller number, larger number).
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2])
    (2.0, 2.2)
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0])
    (2.0, 2.0)
    """
    min_index = 0
    min_value = abs(numbers[min_index] - numbers[min_index + 1])
    for i in range(0, len(numbers) - 1):
        if abs(numbers[i] - numbers[i + 1]) < min_value:
            min_index = i
            min_value = abs(numbers[i] - numbers[i + 1])

    return numbers[min_index], numbers[min_index + 1]
