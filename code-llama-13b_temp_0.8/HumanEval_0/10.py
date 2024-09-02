from typing import List


def has_close_elements(numbers: List[float], threshold: float) -> bool:
    """ Check if in given list of numbers, are any two numbers closer to each other than
    given threshold.
    >>> has_close_elements([1.0, 2.0, 3.0], 0.5)
    False
    >>> has_close_elements([1.0, 2.8, 3.0, 4.0, 5.0, 2.0], 0.3)
    True
    """
    i = 0
    while i < len(numbers):
        num_1 = numbers[i]
        j = i + 1
        while j < len(numbers):
            num_2 = numbers[j]
            if abs(num_1 - num_2) <= threshold:
                return True
            j += 1
        i += 1
    return False
