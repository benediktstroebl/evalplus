from typing import List


def has_close_elements(numbers: List[float], threshold: float) -> bool:
    """ Check if in given list of numbers, are any two numbers closer to each other than
    given threshold.
    >>> has_close_elements([1.0, 2.0, 3.0], 0.5)
    False
    >>> has_close_elements([1.0, 2.8, 3.0, 4.0, 5.0, 2.0], 0.3)
    True
    """
    comparing_index = 1
    while comparing_index < len(numbers):
        first = numbers[comparing_index]
        second = numbers[comparing_index - 1]
        if abs(first - second) <= threshold:
            return True
        comparing_index += 1
    return False

