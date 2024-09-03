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
    length = len(numbers)
    count = 0
    while count < length - 2:
        if abs(numbers[count + 1] - numbers[count + 2]) > threshold:
            if abs(numbers[count + 1] - numbers[count]) < threshold and abs(numbers[count + 2] - numbers[count]) < threshold:
                return True
            else:
                count += 1
    return False

