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

    numbers.sort()  # Sort in place

    if numbers[0] + threshold <= numbers[-1]:
        return True

    for index, current in enumerate(numbers[:-1]):
        next_element = numbers[index + 1]
        if next_element - current > threshold:
            return True

    return False

