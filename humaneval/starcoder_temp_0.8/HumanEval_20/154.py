from typing import List, Tuple


def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    """ From a supplied list of numbers (of length at least two) select and return two that are the closest to each
    other and return them in order (smaller number, larger number).
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2])
    (2.0, 2.2)
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0])
    (2.0, 2.0)
    """
    if not numbers:
        raise ValueError("At least two numbers are required")

    if len(numbers) == 2:
        return numbers

    smallest_index = 0
    smallest_diff = numbers[smallest_index + 1] - numbers[smallest_index]

    for i in range(1, len(numbers) - 1):
        diff = numbers[i + 1] - numbers[i]
        if diff < smallest_diff:
            smallest_index = i
            smallest_diff = diff

    return numbers[smallest_index], numbers[smallest_index + 1]

