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
        raise ValueError
    min_difference = float("inf")
    left = right = None
    for i in range(len(numbers) - 1):
        for j in range(i + 1, len(numbers)):
            difference = numbers[j] - numbers[i]
            if abs(difference) < min_difference:
                min_difference = abs(difference)
                left = numbers[i]
                right = numbers[j]
    return left, right

