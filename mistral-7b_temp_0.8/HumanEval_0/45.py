from typing import List


def has_close_elements(numbers: List[float], threshold: float) -> bool:
    """ Check if in given list of numbers, are any two numbers closer to each other than
    given threshold.
    >>> has_close_elements([1.0, 2.0, 3.0], 0.5)
    False
    >>> has_close_elements([1.0, 2.8, 3.0, 4.0, 5.0, 2.0], 0.3)
    True
    """
    if len(numbers) < 2:
        return False

    min_diff = None
    for i in range(1, len(numbers)):
        current_diff = numbers[i] - numbers[i - 1]
        if current_diff <= threshold and (min_diff is None or min_diff > current_diff):
            min_diff = current_diff

    return min_diff is not None

