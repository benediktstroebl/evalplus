from typing import List, Tuple


def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    """ From a supplied list of numbers (of length at least two) select and return two that are the closest to each
    other and return them in order (smaller number, larger number).
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2])
    (2.0, 2.2)
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0])
    (2.0, 2.0)
    """
    assert len(numbers) >= 2

    diff = numbers[0] - numbers[1]
    min_diff = numbers[0]
    max_diff = numbers[0]
    min_index = 0
    max_index = 0

    for i, number in enumerate(numbers):
        if diff > number - numbers[i - 1]:
            diff = number - numbers[i - 1]
            min_diff = numbers[i - 1]
            max_diff = number
            min_index = i - 1
            max_index = i

    if min_diff == max_diff:
        return min_diff, min_diff
    else:
        return min_diff, max_diff

