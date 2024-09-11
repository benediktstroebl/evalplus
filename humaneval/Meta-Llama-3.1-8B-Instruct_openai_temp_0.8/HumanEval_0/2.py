```python
from typing import List

def has_close_elements(numbers: List[float], threshold: float) -> bool:
    """
    Check if in given list of numbers, are any two numbers closer to each other than given threshold.

    Args:
    numbers (List[float]): A list of floating point numbers.
    threshold (float): The minimum distance between two numbers to be considered close.

    Returns:
    bool: True if there is at least one pair of numbers that are closer than the threshold, False otherwise.
    """
    
    # Sort the list of numbers in ascending order
    numbers.sort()
    
    # Iterate over the sorted list to check for close elements
    for i in range(len(numbers) - 1):
        # Check if the difference between the current and the next number is less than the threshold
        if numbers[i + 1] - numbers[i] < threshold:
            # If close elements are found, return True
            return True
    
    # If no close elements are found, return False
    return False

# Test cases
print(has_close_elements([1.0, 2.0, 3.0], 0.5))  # False
print(has_close_elements([1.0, 2.8, 3.0, 4.0, 5.0, 2.0], 0.3))  # True
```

This script defines a function `has_close_elements` that takes a list of floating point numbers and a threshold as input. It sorts the list and then iterates over it to check for any pair of numbers that are closer together than the specified threshold. If such a pair is found, the function immediately returns `True`; otherwise, it returns `False` after checking all pairs. The test cases at the end demonstrate the function's behavior with various inputs.