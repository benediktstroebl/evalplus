from typing import List


def has_close_elements(numbers: List[float], threshold: float) -> bool:
    """ Check if in given list of numbers, are any two numbers closer to each other than
    given threshold.
    >>> has_close_elements([1.0, 2.0, 3.0], 0.5)
    False
    >>> has_close_elements([1.0, 2.8, 3.0, 4.0, 5.0, 2.0], 0.3)
    True
    """
    numbers_dict = {number: True for number in numbers}
    for number in numbers:
        for another_number in numbers:
            if abs(number - another_number) < threshold:
                if numbers_dict[number] and numbers_dict[another_number]:
                    return True
    return False

