from typing import List


def has_close_elements(numbers: List[float], threshold: float) -> bool:
    """ Check if in given list of numbers, are any two numbers closer to each other than
    given threshold.
    >>> has_close_elements([1.0, 2.0, 3.0], 0.5)
    False
    >>> has_close_elements([1.0, 2.8, 3.0, 4.0, 5.0, 2.0], 0.3)
    True
    """
    # Note: this check could fail if one number is close to zero (the threshold
    # would return True).
    return any(abs(number_a - number_b) <= threshold for number_a, number_b in zip(numbers[:-1], numbers[1:]))

