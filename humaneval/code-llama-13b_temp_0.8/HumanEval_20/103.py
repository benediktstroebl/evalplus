from typing import List, Tuple


def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    """ From a supplied list of numbers (of length at least two) select and return two that are the closest to each
    other and return them in order (smaller number, larger number).
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2])
    (2.0, 2.2)
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0])
    (2.0, 2.0)
    """
    numbers_sorted = sorted(numbers)
    min_numbers = []
    max_numbers = []
    for i in range(len(numbers_sorted) - 1):
        if numbers_sorted[i + 1] - numbers_sorted[i] == min(
            numbers_sorted[i + 1] - numbers_sorted[i], numbers_sorted[i + 1] - numbers_sorted[i]
        ):
            min_numbers.append(numbers_sorted[i])
            max_numbers.append(numbers_sorted[i + 1])
    if len(min_numbers) > 0:
        result = (min(min_numbers), max(max_numbers))
    else:
        result = (numbers_sorted[0], numbers_sorted[1])
    return result

