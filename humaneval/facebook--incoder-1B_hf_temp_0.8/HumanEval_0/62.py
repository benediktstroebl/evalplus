from typing import List


def has_close_elements(numbers: List[float], threshold: float) -> bool:
    """ Check if in given list of numbers, are any two numbers closer to each other than
    given threshold.
    >>> has_close_elements([1.0, 2.0, 3.0], 0.5)
    False
    >>> has_close_elements([1.0, 2.8, 3.0, 4.0, 5.0, 2.0], 0.3)
    True
    """
    sorted_numbers = sorted(numbers)

    # First element is always lower than last one.
    lower = sorted_numbers[0]
    upper = sorted_numbers[-1]

    # Compare numbers.
    if not lower:
        return False
    if not upper:
        return True

    # Compare lower and upper values.
    return abs(lower-upper) < threshold

