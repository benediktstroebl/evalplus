from typing import List
def has_close_elements(numbers: List[float], threshold: float) -> bool:
    """
    Check if in given list of numbers, are any two numbers closer to each other than
    given threshold.
    """
    return any(x - y < threshold for x, y in zip(numbers, numbers[1:]))