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
    if len(numbers) < 2:
        return numbers[0], numbers[0]
    smaller_index = 0
    larger_index = 1
    smaller_diff = abs(numbers[0] - numbers[1])
    larger_diff = abs(numbers[-1] - numbers[-2])
    for index in range(1, len(numbers) - 1):
        current_diff = abs(numbers[index] - numbers[index - 1])
        if current_diff < smaller_diff:
            smaller_index = index
            smaller_diff = current_diff
        current_diff = abs(numbers[index] - numbers[index + 1])
        if current_diff < larger_diff:
            larger_index = index
            larger_diff = current_diff
    return numbers[smaller_index], numbers[
