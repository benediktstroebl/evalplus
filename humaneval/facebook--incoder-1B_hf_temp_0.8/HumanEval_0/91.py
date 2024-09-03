from typing import List


def has_close_elements(numbers: List[float], threshold: float) -> bool:
    """ Check if in given list of numbers, are any two numbers closer to each other than
    given threshold.
    >>> has_close_elements([1.0, 2.0, 3.0], 0.5)
    False
    >>> has_close_elements([1.0, 2.8, 3.0, 4.0, 5.0, 2.0], 0.3)
    True
    """
    close, close_idx = (None, None)
    abs_diff = 0.0
    for a, b in zip(numbers, numbers[1:]):
        diff = abs(a - b)
        if diff <= threshold:
            close_idx = (close_idx, diff)
        elif diff > abs_diff:
            close = (close, diff)
            abs_diff = diff
    return close_idx is not None

