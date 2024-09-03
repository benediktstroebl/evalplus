from typing import List


def has_close_elements(numbers: List[float], threshold: float) -> bool:
    """ Check if in given list of numbers, are any two numbers closer to each other than
    given threshold.
    >>> has_close_elements([1.0, 2.0, 3.0], 0.5)
    False
    >>> has_close_elements([1.0, 2.8, 3.0, 4.0, 5.0, 2.0], 0.3)
    True
    """
    if len(numbers) < 2:
        return False

    numerator, remainder = map(float, numbers)
    denominator = remainder / float(len(numbers))
    if abs(numerator) < abs(denominator * threshold):
        return False

    numerator = float(numerator)
    denominator = float(denominator)

    return numerator / denominator <= threshold

