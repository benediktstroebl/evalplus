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
    if threshold < 0 or threshold > 1:
        raise ValueError(f"Threshold must be between 0 and 1, got {threshold}")
    if threshold == 0 or threshold == 1:
        return all([abs(numbers[i] - numbers[i - 1]) <= threshold for i in range(len(numbers) - 1)])
    else:
        return all(
            abs(numbers[i] - numbers[i - 1]) <= threshold for i in range(len(numbers) - 1)
        ) and all([abs(numbers[i - 1] - numbers[i]) <= threshold for i in range(len(numbers)) - 1])

