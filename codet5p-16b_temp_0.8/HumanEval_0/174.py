from typing import List


def has_close_elements(numbers: List[float], threshold: float) -> bool:
    """ Check if in given list of numbers, are any two numbers closer to each other than
    given threshold.
    >>> has_close_elements([1.0, 2.0, 3.0], 0.5)
    False
    >>> has_close_elements([1.0, 2.8, 3.0, 4.0, 5.0, 2.0], 0.3)
    True
    """

    for i, first in enumerate(numbers):
        for second in numbers[i + 1:]:
            if abs(first - second) < threshold:
                return True
    return False
    # TODO: Write code that checks if in given list of numbers, are any two numbers closer to each other than
    # given threshold.
    #
    # If the absolute difference between two numbers is less than the given threshold, then they are considered "close enough".
    #
    # >>> has_close_elements([1.0, 2.8, 3.0, 4.0, 5.0, 2.0], 0.3)
    # True

