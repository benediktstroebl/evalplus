from typing import List, Tuple


def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    """ From a supplied list of numbers (of length at least two) select and return two that are the closest to each
    other and return them in order (smaller number, larger number).
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2])
    (2.0, 2.2)
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0])
    (2.0, 2.0)
    """
    if len(numbers) <= 2:
        return numbers[0], numbers[1]

    current_diff = numbers[1] - numbers[0]
    min_diff = current_diff
    min_index = 1

    for i in range(2, len(numbers)):
        diff = numbers[i] - numbers[i - 1]
        if diff < min_diff:
            min_diff = diff
            min_index = i

    return numbers[min_index - 1], numbers[min_index]

