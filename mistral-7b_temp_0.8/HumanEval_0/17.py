from typing import List


def has_close_elements(numbers: List[float], threshold: float) -> bool:
    """ Check if in given list of numbers, are any two numbers closer to each other than
    given threshold.
    >>> has_close_elements([1.0, 2.0, 3.0], 0.5)
    False
    >>> has_close_elements([1.0, 2.8, 3.0, 4.0, 5.0, 2.0], 0.3)
    True
    """
    # 1. loop through each element
    # 2. check if there are any elements closer to it than threshold
    for element in numbers:
        # 3. loop through each element again
        for check_element in numbers:
            if abs(element - check_element) < threshold:
                return True

    return False
