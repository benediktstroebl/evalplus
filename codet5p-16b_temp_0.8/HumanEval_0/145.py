from typing import List


def has_close_elements(numbers: List[float], threshold: float) -> bool:
    """ Check if in given list of numbers, are any two numbers closer to each other than
    given threshold.
    >>> has_close_elements([1.0, 2.0, 3.0], 0.5)
    False
    >>> has_close_elements([1.0, 2.8, 3.0, 4.0, 5.0, 2.0], 0.3)
    True
    """

    sorted_numbers = sorted(numbers)
    for index, num in enumerate(sorted_numbers):
        if index == 0:
            continue
        next_num = sorted_numbers[index]
        if abs(num - next_num) < threshold:
            return True
    return False
