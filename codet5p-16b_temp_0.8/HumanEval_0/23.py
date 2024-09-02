from typing import List


def has_close_elements(numbers: List[float], threshold: float) -> bool:
    """ Check if in given list of numbers, are any two numbers closer to each other than
    given threshold.
    >>> has_close_elements([1.0, 2.0, 3.0], 0.5)
    False
    >>> has_close_elements([1.0, 2.8, 3.0, 4.0, 5.0, 2.0], 0.3)
    True
    """

    if len(numbers) <= 1:
        return False
    last_pair = numbers[0] - numbers[1]
    for i in range(len(numbers) - 1):
        current_pair = numbers[i] - numbers[i + 1]
        if current_pair <= threshold or last_pair <= threshold:
            return True
        last_pair = current_pair
    return False
