from typing import List


def has_close_elements(numbers: List[float], threshold: float) -> bool:
    """ Check if in given list of numbers, are any two numbers closer to each other than
    given threshold.
    >>> has_close_elements([1.0, 2.0, 3.0], 0.5)
    False
    >>> has_close_elements([1.0, 2.8, 3.0, 4.0, 5.0, 2.0], 0.3)
    True
    """
    current_min = None
    for current_number in numbers:
        if current_min is None or current_number < current_min:
            current_min = current_number

    for current_number in numbers:
        diff = current_number - current_min
        if abs(diff) < threshold:
            return True

    return False

