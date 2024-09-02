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
    start_index = 0
    end_index = len(numbers) - 1
    while start_index < end_index:
        if abs(numbers[start_index] - numbers[end_index]) <= 0.00001:  # PEP8: use modern style comparison (a > b, not a < b)
            return numbers[start_index], numbers[end_index]
        middle_index = (start_index + end_index) // 2
        if abs(numbers[middle_index] - numbers[end_index]) >= abs(numbers[start_index] - numbers[middle_index]):
            start_index = middle_index + 1
        else:
            end_index = middle_index - 1
    return numbers[start_index], numbers[end_index]

