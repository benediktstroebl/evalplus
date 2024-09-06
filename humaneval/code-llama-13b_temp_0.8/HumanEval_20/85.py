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
    closest_diff = numbers_sorted[1] - numbers_sorted[0]
    for i in range(1, len(numbers_sorted) - 1):
        if numbers_sorted[i + 1] - numbers_sorted[i - 1] < closest_diff:
            closest_diff = numbers_sorted[i + 1] - numbers_sorted[i - 1]
            first_element = numbers_sorted[i + 1]
            second_element = numbers_sorted[i - 1]
    if first_element == second_element:
        first_element = numbers_sorted[0]
        second_element = numbers_sorted[1]
    return first_element, second_element

