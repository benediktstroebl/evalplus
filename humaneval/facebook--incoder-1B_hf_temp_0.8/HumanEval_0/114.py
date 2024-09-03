from typing import List


def has_close_elements(numbers: List[float], threshold: float) -> bool:
    """ Check if in given list of numbers, are any two numbers closer to each other than
    given threshold.
    >>> has_close_elements([1.0, 2.0, 3.0], 0.5)
    False
    >>> has_close_elements([1.0, 2.8, 3.0, 4.0, 5.0, 2.0], 0.3)
    True
    """
    length = len(numbers)
    threshold = np.deg2rad(threshold)
    threshold = min(max(threshold, 0), length - 1)

    # noinspection PyTypeChecker
    for i in range(len(numbers)):
        if np.rad2deg(abs(numbers[i] - numbers[i + 1])) <= threshold:
            return False
    return True

