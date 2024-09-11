```python
from typing import List

def has_close_elements(numbers: List[float], threshold: float) -> bool:
    """
    Check if in given list of numbers, are any two numbers closer to each other than given threshold.

    Args:
        numbers (List[float]): A list of floating-point numbers.
        threshold (float): The minimum distance required between two numbers.

    Returns:
        bool: True if any two numbers are closer to each other than the given threshold, False otherwise.
    """
    # Sort the list of numbers in ascending order
    sorted_numbers = sorted(numbers)

    # Iterate over the sorted list of numbers
    for i in range(len(sorted_numbers) - 1):
        # Calculate the difference between the current number and the next number
        difference = sorted_numbers[i + 1] - sorted_numbers[i]

        # If the difference is less than the threshold, return True
        if difference < threshold:
            return True

    # If no pair of numbers is closer than the threshold, return False
    return False


# Example usage:
print(has_close_elements([1.0, 2.0, 3.0], 0.5))  # Output: False
print(has_close_elements([1.0, 2.8, 3.0, 4.0, 5.0, 2.0], 0.3))  # Output: True
```

This script defines a function `has_close_elements` that takes a list of numbers and a threshold value as input. It sorts the list of numbers and then iterates over it to check if any two numbers are closer to each other than the given threshold. If such a pair is found, the function returns `True`; otherwise, it returns `False`. The example usage at the end demonstrates how to call the function with different inputs.