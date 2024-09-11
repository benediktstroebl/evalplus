```python
from typing import List

def has_close_elements(numbers: List[float], threshold: float) -> bool:
    """
    Check if in given list of numbers, are any two numbers closer to each other than
    given threshold.

    Args:
    numbers (List[float]): A list of float numbers.
    threshold (float): The threshold value.

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
        diff = numbers[i] - numbers[i-1]
        
        # Update the minimum difference if the current difference is smaller
        min_diff = min(min_diff, diff)
        
        # If the minimum difference is less than or equal to the threshold, return True
        if min_diff <= threshold:
            return True
    
    # If no two numbers are closer than the threshold, return False
    return False

# Test cases
print(has_close_elements([1.0, 2.0, 3.0], 0.5))  # False
print(has_close_elements([1.0, 2.8, 3.0, 4.0, 5.0, 2.0], 0.3))  # True
```

This script defines a function `has_close_elements` that takes a list of float numbers and a threshold value as input, and returns a boolean indicating whether any two numbers in the list are closer to each other than the given threshold. The function sorts the list of numbers, iterates over the sorted list to find the minimum difference between any two numbers, and returns True if the minimum difference is less than or equal to the threshold, False otherwise.