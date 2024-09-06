from typing import List
import unittest
def has_close_elements(numbers: List[float], threshold: float) -> bool:
    """
    Check if in given list of numbers, are any two numbers closer to each other than
    given threshold.
    """
    # Initialize a flag to track if any two numbers are close enough
    has_close_elements = False

    # Iterate over all pairs of numbers in the list
    for i in range(len(numbers)-1):
        for j in range(i+1, len(numbers)):
            if abs(numbers[i] - numbers[j]) < threshold:
                has_close_elements = True
                # Exit the nested loop as soon as a pair is found
                break

    return has_close_elements