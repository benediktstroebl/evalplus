from typing import List


def has_close_elements(numbers: List[float], threshold: float) -> bool:
    """ Check if in given list of numbers, are any two numbers closer to each other than
    given threshold.
    >>> has_close_elements([1.0, 2.0, 3.0], 0.5)
    False
    >>> has_close_elements([1.0, 2.8, 3.0, 4.0, 5.0, 2.0], 0.3)
    True
    """
    # check if a number is followed by a number that is closer than the threshold
    # check if a number is preceded by a number that is closer than the threshold
    for i in range(1, len(numbers)):
        if abs(numbers[i] - numbers[i - 1]) < threshold:
            return True
    return False

