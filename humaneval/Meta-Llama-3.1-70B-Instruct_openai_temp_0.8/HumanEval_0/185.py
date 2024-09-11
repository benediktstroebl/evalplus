```python
from typing import List

def has_close_elements(numbers: List[float], threshold: float) -> bool:
    """
    Check if in given list of numbers, are any two numbers closer to each other than
    given threshold.

    Args:
        numbers (List[float]): A list of floating point numbers.
        threshold (float): The maximum allowed distance between two numbers.

    Returns:
        bool: True if at least two numbers are closer than the threshold, False otherwise.
    """
    # Sort the list of numbers in ascending order
    numbers.sort()

    # Iterate over the sorted list of numbers
    for i in range(len(numbers) - 1):
        # Calculate the difference between the current number and the next number
        difference = numbers[i + 1] - numbers[i]
        
        # If the difference is less than or equal to the threshold, return True
        if difference <= threshold:
            return True

    # If no two numbers are closer than the threshold, return False
    return False


# Test cases
print(has_close_elements([1.0, 2.0, 3.0], 0.5))  # Expected output: False
print(has_close_elements([1.0, 2.8, 3.0, 4.0, 5.0, 2.0], 0.3))  # Expected output: True
```

This script defines a function `has_close_elements` that takes a list of floating point numbers and a threshold as input, and returns `True` if at least two numbers in the list are closer than the threshold, and `False` otherwise. The function sorts the list of numbers in ascending order, then iterates over the sorted list to find the smallest difference between two consecutive numbers. If the smallest difference is less than or equal to the threshold, the function returns `True`. Otherwise, it returns `False`. The script also includes two test cases to demonstrate the function's behavior.