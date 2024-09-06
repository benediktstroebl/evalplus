from typing import List


def has_close_elements(numbers: List[float], threshold: float) -> bool:
    """ Check if in given list of numbers, are any two numbers closer to each other than
    given threshold.
    >>> has_close_elements([1.0, 2.0, 3.0], 0.5)
    False
    >>> has_close_elements([1.0, 2.8, 3.0, 4.0, 5.0, 2.0], 0.3)
    True
    """
    first_diff = max(numbers[0] - numbers[1], numbers[0] - numbers[2])
    second_diff = max(numbers[2] - numbers[3], numbers[3] - numbers[4])
    for i in range(1, len(numbers)):
        third_diff = max(numbers[i] - numbers[i+1], numbers[i] - numbers[i-1])
        if first_diff + third_diff <= threshold:
            return False
    return True
