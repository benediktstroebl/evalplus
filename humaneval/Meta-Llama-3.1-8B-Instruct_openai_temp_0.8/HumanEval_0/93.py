```python
from typing import List

def has_close_elements(numbers: List[float], threshold: float) -> bool:
    """
    Check if in given list of numbers, are any two numbers closer to each other than given threshold.

    Args:
        numbers (List[float]): A list of floating point numbers.
        threshold (float): The minimum distance required between two numbers.

    Returns:
        bool: True if any two numbers are closer than the threshold, False otherwise.
    """
    # Sort the list of numbers
    sorted_numbers = sorted(numbers)
    
    # Iterate over the sorted list to compare adjacent numbers
    for i in range(len(sorted_numbers) - 1):
        # Check if the difference between two adjacent numbers is less than the threshold
        if sorted_numbers[i + 1] - sorted_numbers[i] < threshold:
            return True
    
    # If no pair of adjacent numbers is closer than the threshold, return False
    return False

# Test cases
if has_close_elements([1.0, 2.0, 3.0], 0.5):
    print("Test case 1 failed")
else:
    print("Test case 1 passed")

if has_close_elements([1.0, 2.8, 3.0, 4.0, 5.0, 2.0], 0.3):
    print("Test case 2 failed")
else:
    print("Test case 2 passed")
```

This script defines a function `has_close_elements` that takes a list of numbers and a threshold as input, sorts the list, and then iterates over the sorted list to check if any two adjacent numbers are closer than the threshold. If such a pair is found, the function returns `True`; otherwise, it returns `False`. The script also includes two test cases to verify the function's correctness.