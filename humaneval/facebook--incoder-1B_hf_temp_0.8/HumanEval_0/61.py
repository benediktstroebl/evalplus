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
    threshold = float(threshold)

    if numbers:
        last_number = numbers[0]
        for number in numbers[1:]:
            if abs(number - last_number) < threshold:
                return False
            last_number = number

    return True

