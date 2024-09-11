```python
from typing import List

def has_close_elements(numbers: List[float], threshold: float) -> bool:
    """
    Check if in given list of numbers, are any two numbers closer to each other than given threshold.

    Args:
    numbers (List[float]): A list of floating point numbers.
    threshold (float): The minimum distance between two numbers to be considered close.

    Returns:
    bool: True if any two numbers are closer than the threshold, False otherwise.
    """
    # Sort the list of numbers to make it easier to compare adjacent elements
    numbers.sort()
    
    # Iterate over the sorted list, comparing each number with its predecessor
    for i in range(1, len(numbers)):
        # If the difference between the current number and its predecessor is less than the threshold
        if numbers[i] - numbers[i-1] < threshold:
            # Return True, because we found two numbers that are closer than the threshold
            return True
    
    # If we iterated over the entire list without finding any close elements, return False
    return False

# Test cases
if has_close_elements([1.0, 2.0, 3.0], 0.5):
    print("Test case 1 failed: Expected False, got True")
else:
    print("Test case 1 passed")

if has_close_elements([1.0, 2.8, 3.0, 4.0, 5.0, 2.0], 0.3):
    print("Test case 2 passed")
else:
    print("Test case 2 failed: Expected True, got False")
```

This script uses a simple sorting-based approach to solve the problem. It sorts the list of numbers and then iterates over the sorted list, comparing each number with its predecessor. If it finds two numbers that are closer than the threshold, it immediately returns True. If it iterates over the entire list without finding any close elements, it returns False.