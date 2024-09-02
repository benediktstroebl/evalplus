from typing import List


def has_close_elements(numbers: List[float], threshold: float) -> bool:
    """ Check if in given list of numbers, are any two numbers closer to each other than
    given threshold.
    >>> has_close_elements([1.0, 2.0, 3.0], 0.5)
    False
    >>> has_close_elements([1.0, 2.8, 3.0, 4.0, 5.0, 2.0], 0.3)
    True
    """
    for number_index in range(len(numbers)):
        for other_number_index in range(len(numbers)):
            if number_index == other_number_index:
                continue
            if abs(numbers[number_index] - numbers[other_number_index]) < threshold:
                return True
    return False

