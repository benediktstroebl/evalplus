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
    numbers_sorted = sorted(numbers)
    numbers_diff = numbers_sorted[1:] - numbers_sorted[:-1]
    for x in numbers_diff:
        if abs(x - numbers[0]) <= threshold:
            return True
    return False
