### Self-Contained Python Script
```python
from typing import List

def has_close_elements(numbers: List[float], threshold: float) -> bool:
    """
    Check if in given list of numbers, are any two numbers closer to each other than
    given threshold.

    Args:
        numbers (List[float]): A list of floating point numbers.
        threshold (float): The threshold value to check closeness.

    Returns:
        bool: True if any two numbers are closer than the threshold, False otherwise.
    """
    # First, sort the list of numbers in ascending order
    numbers.sort()

    # Initialize the minimum difference as infinity
    min_diff = float('inf')

    # Iterate over the sorted list of numbers
    for i in range(1, len(numbers)):
        # Calculate the difference between the current number and the previous number
        diff = numbers[i] - numbers[i - 1]
        
        # Update the minimum difference if the current difference is smaller
        if diff < min_diff:
            min_diff = diff

    # Return True if the minimum difference is less than or equal to the threshold
    return min_diff <= threshold


# Test cases
print(has_close_elements([1.0, 2.0, 3.0], 0.5))  # False
print(has_close_elements([1.0, 2.8, 3.0, 4.0, 5.0, 2.0], 0.3))  # True
```

This Python script defines a function `has_close_elements` that checks if any two numbers in a given list are closer to each other than a specified threshold. It uses sorting to bring close numbers together and then iterates over the sorted list to find the minimum difference. The function returns `True` if the minimum difference is less than or equal to the threshold and `False` otherwise. The script includes test cases to demonstrate its usage.