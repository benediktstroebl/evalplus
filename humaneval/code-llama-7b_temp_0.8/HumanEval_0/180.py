from typing import List


def has_close_elements(numbers: List[float], threshold: float) -> bool:
    """ Check if in given list of numbers, are any two numbers closer to each other than
    given threshold.
    >>> has_close_elements([1.0, 2.0, 3.0], 0.5)
    False
    >>> has_close_elements([1.0, 2.8, 3.0, 4.0, 5.0, 2.0], 0.3)
    True
    """

    min_num = min(numbers)
    max_num = max(numbers)

    for num in numbers:
        if abs(min_num - num) < threshold or abs(max_num - num) < threshold:
            return True

    return False

