from hypothesis import given, settings, strategies as st
from typing import List
def has_close_elements(numbers: List[float], threshold: float) -> bool:
    """
    Check if in given list of numbers, are any two numbers closer to each other than
    given threshold.
    """
    # Using NaN as a starting value to check if any number is NaN first
    closest_num = float('nan')
    for num in numbers:
        # If current number is NaN, skip calculation
        if num != num:
            continue
        # Otherwise check if it's closer than current closest_num
        if abs(num - closest_num) < threshold:
            closest_num = num
    return bool(closest_num != float('nan'))