from typing import List


def has_close_elements(numbers: List[float], threshold: float) -> bool:
    """ Check if in given list of numbers, are any two numbers closer to each other than
    given threshold.
    >>> has_close_elements([1.0, 2.0, 3.0], 0.5)
    False
    >>> has_close_elements([1.0, 2.8, 3.0, 4.0, 5.0, 2.0], 0.3)
    True
    """
    if not numbers:
        return False
    closer_than = abs(numbers[0] - numbers[1]) < threshold
    closer_than_or_equal_1 = abs(numbers[0] - numbers[1]) >= threshold
    closer_than_or_equal_2 = abs(numbers[0] - numbers[1]) >= threshold
    return closer_than or closer_than_or_equal_1 or closer_than_or_equal_2

