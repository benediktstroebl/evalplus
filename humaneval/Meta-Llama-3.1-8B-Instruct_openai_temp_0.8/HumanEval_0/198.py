```python
from typing import List

def has_close_elements(numbers: List[float], threshold: float) -> bool:
    """
    Check if in given list of numbers, are any two numbers closer to each other than
    given threshold.

    Args:
    numbers (List[float]): A list of floating point numbers.
    threshold (float): The minimum distance between two numbers to be considered close.

    Returns:
    bool: True if there are any two numbers in the list closer than the given threshold, False otherwise.
    """
    
    # Sort the list of numbers in ascending order
    numbers.sort()
    
    # Iterate over the sorted list of numbers
    for i in range(len(numbers) - 1):
        # Check if the difference between the current number and the next number is less than or equal to the threshold
        if numbers[i + 1] - numbers[i] <= threshold:
            # If the difference is less than or equal to the threshold, return True
            return True
    
    # If the loop completes without finding any two numbers closer than the threshold, return False
    return False

# Test cases
if has_close_elements([1.0, 2.0, 3.0], 0.5):
    print("Test case 1 failed - expected False, got True")
else:
    print("Test case 1 passed")

if not has_close_elements([1.0, 2.8, 3.0, 4.0, 5.0, 2.0], 0.3):
    print("Test case 2 failed - expected True, got False")
else:
    print("Test case 2 passed")
```

This script defines a function `has_close_elements` that checks if there are any two numbers in the list `numbers` that are closer than the given `threshold`. It sorts the list of numbers and then iterates over the sorted list to check the difference between each pair of adjacent numbers. If it finds any pair of numbers with a difference less than or equal to the threshold, it returns `True`. Otherwise, it returns `False`. The test cases at the end of the script verify that the function behaves correctly for the given examples.