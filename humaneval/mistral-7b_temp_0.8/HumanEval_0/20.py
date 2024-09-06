from typing import List


def has_close_elements(numbers: List[float], threshold: float) -> bool:
    """ Check if in given list of numbers, are any two numbers closer to each other than
    given threshold.
    >>> has_close_elements([1.0, 2.0, 3.0], 0.5)
    False
    >>> has_close_elements([1.0, 2.8, 3.0, 4.0, 5.0, 2.0], 0.3)
    True
    """
    previous_number = None

    for current_number in numbers:
        if previous_number is not None:
            distance = abs(previous_number - current_number)
            if distance < threshold:
                return True
        previous_number = current_number
    return False

