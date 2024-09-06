from typing import List


def has_close_elements(numbers: List[float], threshold: float) -> bool:
    """ Check if in given list of numbers, are any two numbers closer to each other than
    given threshold.
    >>> has_close_elements([1.0, 2.0, 3.0], 0.5)
    False
    >>> has_close_elements([1.0, 2.8, 3.0, 4.0, 5.0, 2.0], 0.3)
    True
    """
    numbers_set = set(numbers)
    for i in numbers:
        for j in numbers:
            if abs(i - j) < threshold:
                if (i, j) in numbers_set or (j, i) in numbers_set:
                    return True

    return False

