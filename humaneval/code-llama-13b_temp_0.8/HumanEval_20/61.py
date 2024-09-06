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
    min_index = 0
    max_index = 0
    min_diff = numbers[max_index] - numbers[min_index]
    for i in range(1, len(numbers)):
        current_diff = numbers[i] - numbers[i - 1]
        if current_diff < min_diff:
            min_diff = current_diff
            min_index = i - 1
            max_index = i
    return numbers[min_index], numbers[max_index]

