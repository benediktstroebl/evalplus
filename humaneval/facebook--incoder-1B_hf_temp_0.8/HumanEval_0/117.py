from typing import List


def has_close_elements(numbers: List[float], threshold: float) -> bool:
    """ Check if in given list of numbers, are any two numbers closer to each other than
    given threshold.
    >>> has_close_elements([1.0, 2.0, 3.0], 0.5)
    False
    >>> has_close_elements([1.0, 2.8, 3.0, 4.0, 5.0, 2.0], 0.3)
    True
    """
    # sort given list of numbers
    numbers.sort()

    # split given list of numbers into two groups:
    # 1. all numbers which are less than threshold
    # 2. all numbers which are greater than threshold
    left_half = numbers[::2]
    right_half = numbers[1::2]

    # calculate difference of left and right half values
    left_diff = left_half - threshold
    right_diff = right_half - threshold

    return any(abs(left_diff) < abs(right_diff))

