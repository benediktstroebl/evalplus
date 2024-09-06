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
        raise ValueError('List must be at least two numbers')
    min_diff = None
    for i in range(len(numbers) - 1):
        for j in range(i + 1, len(numbers)):
            diff = numbers[i] - numbers[j]
            if min_diff is None or diff < min_diff:
                min_diff = diff
                first = numbers[i]
                second = numbers[j]
    return first, second

