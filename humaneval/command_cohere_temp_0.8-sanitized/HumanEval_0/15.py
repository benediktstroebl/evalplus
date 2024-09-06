from typing import List
def has_close_elements(numbers: List[float], threshold: float) -> bool:
    """
    Check if in given list of numbers, are any two numbers closer to each other than
    given threshold.
    """
    return any(abs(x - y) < threshold for i, x in enumerate(numbers) for j, y in enumerate(numbers[i + 1:], i + 1) if x < y and abs(x - y) < threshold)