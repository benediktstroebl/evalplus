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
        return None, None
    if len(numbers) == 1:
        return numbers[0], numbers[0]

    low_index, low_diff = 0, numbers[1] - numbers[0]
    high_index, high_diff = 1, numbers[-1] - numbers[0]

    for i in range(1, len(numbers)):
        diff = numbers[i] - numbers[0]
        if diff < low_diff:
            low_diff = diff
            low_index = i
        elif diff > high_diff:
            high_diff = diff
            high_index = i

    return numbers[low_index], numbers[high_index]

