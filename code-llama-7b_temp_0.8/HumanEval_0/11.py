from typing import List


def has_close_elements(numbers: List[float], threshold: float) -> bool:
    """ Check if in given list of numbers, are any two numbers closer to each other than
    given threshold.
    >>> has_close_elements([1.0, 2.0, 3.0], 0.5)
    False
    >>> has_close_elements([1.0, 2.8, 3.0, 4.0, 5.0, 2.0], 0.3)
    True
    """
    if len(numbers) <= 1:
        return False

    numbers_sorted = sorted(numbers)

    for i, n in enumerate(numbers_sorted):
        if abs(numbers_sorted[i] - numbers_sorted[i + 1]) < threshold:
            return True
    return False

