```python
from typing import List

def has_close_elements(numbers: List[float], threshold: float) -> bool:
    """
    Check if in given list of numbers, are any two numbers closer to each other than
    given threshold.

    Args:
        numbers (List[float]): A list of floating point numbers.
        threshold (float): The minimum distance required between two numbers.

    Returns:
        bool: True if any two numbers are closer than the threshold, False otherwise.
    """
    # First, sort the list of numbers
    numbers.sort()

    # Initialize the minimum difference to infinity
    min_diff = float('inf')

    # Iterate through the sorted list to find the minimum difference
    for i in range(1, len(numbers)):
        # Calculate the difference between the current number and the previous one
        diff = numbers[i] - numbers[i - 1]
        
        # Update the minimum difference if the current difference is smaller
        if diff < min_diff:
            min_diff = diff

    # Return True if the minimum difference is less than or equal to the threshold
    return min_diff <= threshold


# Test cases
print(has_close_elements([1.0, 2.0, 3.0], 0.5))  # False
print(has_close_elements([1.0, 2.8, 3.0, 4.0, 5.0, 2.0], 0.3))  # True
print(has_close_elements([1.0, 2.0, 3.0, 4.0, 5.0], 2.5))  # False
print(has_close_elements([1.0, 1.1, 3.0, 4.0, 5.0], 0.5))  # True
```