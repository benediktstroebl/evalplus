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
    numbers.sort()  # Sort the list of numbers in ascending order
    for i in range(1, len(numbers)):  # Iterate over the sorted list
        if numbers[i] - numbers[i - 1] <= threshold:  # Check if the difference between two adjacent numbers is less than or equal to the threshold
            return True  # If a pair of numbers is closer than the threshold, return True
    return False  # If no such pair is found, return False

# Test cases
print(has_close_elements([1.0, 2.0, 3.0], 0.5))  # Expected output: False
print(has_close_elements([1.0, 2.8, 3.0, 4.0, 5.0, 2.0], 0.3))  # Expected output: True
print(has_close_elements([1.0, 2.0, 3.0, 4.0, 5.0], 1.0))  # Expected output: False
print(has_close_elements([1.0, 2.0, 2.0, 3.0], 0.5))  # Expected output: True
```

This script defines a function `has_close_elements` that takes a list of floating point numbers and a threshold as input, and returns a boolean indicating whether any two numbers in the list are closer than the threshold. The function first sorts the list of numbers, and then iterates over the sorted list to check if any two adjacent numbers are closer than the threshold. If such a pair is found, the function returns True; otherwise, it returns False. The script also includes test cases to demonstrate the function's behavior.