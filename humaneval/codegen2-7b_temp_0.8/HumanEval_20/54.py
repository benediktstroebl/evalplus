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
        return 0, 0
    min_diff = 100
    min_index = 0
    for index, number in enumerate(numbers):
        diff = abs(number - numbers[min_index])
        if diff < min_diff:
            min_diff = diff
            min_index = index
    return numbers[min_index], numbers[min_
