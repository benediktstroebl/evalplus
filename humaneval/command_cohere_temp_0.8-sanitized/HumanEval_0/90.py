from typing import List
import unittest
def has_close_elements(numbers: List[float], threshold: float) -> bool:
    """
    Check if in given list of numbers, are any two numbers closer to each other than
    given threshold.
    """
    # Sort the list naturally to use the tuple as key for NaN-safe equality check
    sorted_nums = sorted(numbers)
    for i in range(len(sorted_nums) - 1):
        # Found two numbers with threshold or smaller distance
        if sorted_nums[i + 1] - sorted_nums[i] <= threshold:
            return True
    return False