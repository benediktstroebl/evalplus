from typing import List


def has_close_elements(numbers: List[float], threshold: float) -> bool:
    """ Check if in given list of numbers, are any two numbers closer to each other than
    given threshold.
    >>> has_close_elements([1.0, 2.0, 3.0], 0.5)
    False
    >>> has_close_elements([1.0, 2.8, 3.0, 4.0, 5.0, 2.0], 0.3)
    True
    """
    numbers = sorted(numbers)
    for index, number in enumerate(numbers):
        next_index = index + 1
        try:
            next_number = numbers[next_index]
            if next_number - number < threshold:
                return True
        except IndexError:
            pass
    return False

