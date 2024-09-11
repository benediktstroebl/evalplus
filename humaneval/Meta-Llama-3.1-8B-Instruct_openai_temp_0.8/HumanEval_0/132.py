```python
from typing import List

def has_close_elements(numbers: List[float], threshold: float) -> bool:
    """
    Check if in given list of numbers, are any two numbers closer to each other than given threshold.

    Args:
        numbers (List[float]): A list of floating point numbers.
        threshold (float): The minimum distance between two numbers to be considered as not close.

    Returns:
        bool: True if any two numbers in the list are closer than the threshold, False otherwise.
    """
    numbers.sort()  # Sort the list to simplify the comparison

    for i in range(1, len(numbers)):
        # Check if the difference between the current number and the previous number is less than the threshold
        if numbers[i] - numbers[i - 1] < threshold:
            return True  # If close, immediately return True

    return False  # If no close elements are found after iterating through the list

# Example usage
print(has_close_elements([1.0, 2.0, 3.0], 0.5))  # False
print(has_close_elements([1.0, 2.8, 3.0, 4.0, 5.0, 2.0], 0.3))  # True
```

This script defines a function `has_close_elements` that takes a list of floats and a threshold as input. It sorts the list and then iterates over it, checking if the difference between each pair of consecutive numbers is less than the threshold. If it finds any such pair, it immediately returns `True`. If it finishes iterating over the list without finding any close elements, it returns `False`. The example usage demonstrates how to use this function with the provided test cases.