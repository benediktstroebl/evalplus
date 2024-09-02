from typing import List


def has_close_elements(numbers: List[float], threshold: float) -> bool:
    """ Check if in given list of numbers, are any two numbers closer to each other than
    given threshold.
    >>> has_close_elements([1.0, 2.0, 3.0], 0.5)
    False
    >>> has_close_elements([1.0, 2.8, 3.0, 4.0, 5.0, 2.0], 0.3)
    True
    """
    closest_diff = float('inf')
    for num1, num2 in zip(numbers, numbers[1:]+numbers):
        diff = abs(num1 - num2)
        if diff < closest_diff:
            closest_diff = diff
            closest_num1, closest_num2 = num1, num2
    return closest_diff <= threshold

