from typing import List


def has_close_elements(numbers: List[float], threshold: float) -> bool:
    """ Check if in given list of numbers, are any two numbers closer to each other than
    given threshold.
    >>> has_close_elements([1.0, 2.0, 3.0], 0.5)
    False
    >>> has_close_elements([1.0, 2.8, 3.0, 4.0, 5.0, 2.0], 0.3)
    True
    """
    if len(numbers) == 2:
        if numbers[0] < numbers[1] and numbers[0] == numbers[1]:
            return True
        elif numbers[1] < numbers[0] and numbers[1] == numbers[0]:
            return True
    return False

