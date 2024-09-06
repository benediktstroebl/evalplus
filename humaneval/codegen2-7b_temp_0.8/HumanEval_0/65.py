from typing import List


def has_close_elements(numbers: List[float], threshold: float) -> bool:
    """ Check if in given list of numbers, are any two numbers closer to each other than
    given threshold.
    >>> has_close_elements([1.0, 2.0, 3.0], 0.5)
    False
    >>> has_close_elements([1.0, 2.8, 3.0, 4.0, 5.0, 2.0], 0.3)
    True
    """
    if len(numbers) <= 2:
        return False
    
    for idx, num in enumerate(numbers):
        for idx_2 in range(idx+1, len(numbers)):
            if (num - numbers[idx_2]).abs() <= threshold:
                return True
    return
