from typing import List


def has_close_elements(numbers: List[float], threshold: float) -> bool:
    """ Check if in given list of numbers, are any two numbers closer to each other than
    given threshold.
    >>> has_close_elements([1.0, 2.0, 3.0], 0.5)
    False
    >>> has_close_elements([1.0, 2.8, 3.0, 4.0, 5.0, 2.0], 0.3)
    True
    """
    diffs = [abs(x - y) for x, y in zip(numbers, numbers[1:])]
    diffs.sort()
    diff_threshold = threshold / diffs[-1]
    for diff in diffs:
        if abs(diff) <= diff_threshold:
            return True
    return False

