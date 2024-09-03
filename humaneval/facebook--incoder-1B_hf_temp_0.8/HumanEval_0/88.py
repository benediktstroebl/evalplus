from typing import List


def has_close_elements(numbers: List[float], threshold: float) -> bool:
    """ Check if in given list of numbers, are any two numbers closer to each other than
    given threshold.
    >>> has_close_elements([1.0, 2.0, 3.0], 0.5)
    False
    >>> has_close_elements([1.0, 2.8, 3.0, 4.0, 5.0, 2.0], 0.3)
    True
    """
    if len(numbers) == 0:
        return False

    closest_diff = abs(numbers[0] - numbers[-1])
    diffs = [abs(number - numbers[-1]) for number in numbers]
    thresh_thresh = abs(threshold * 2)

    return all(diff < thresh_thresh for diff in diffs) and closest_diff < thresh_thresh

