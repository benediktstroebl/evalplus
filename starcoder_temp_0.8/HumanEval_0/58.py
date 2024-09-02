from typing import List


def has_close_elements(numbers: List[float], threshold: float) -> bool:
    """ Check if in given list of numbers, are any two numbers closer to each other than
    given threshold.
    >>> has_close_elements([1.0, 2.0, 3.0], 0.5)
    False
    >>> has_close_elements([1.0, 2.8, 3.0, 4.0, 5.0, 2.0], 0.3)
    True
    """
    numbers_dict = {}
    for i in range(len(numbers)):
        numbers_dict[numbers[i]] = 1
    for key, value in numbers_dict.items():
        if key - threshold in numbers_dict:
            return True
        if key + threshold in numbers_dict:
            return True
    return False

