```python
from typing import List

def has_close_elements(numbers: List[float], threshold: float) -> bool:
    """
    Check if in given list of numbers, are any two numbers closer to each other than given threshold.

    Args:
    numbers (List[float]): A list of floating point numbers.
    threshold (float): The minimum distance between two numbers.

    Returns:
    bool: True if any two numbers are closer than the threshold, False otherwise.
    """
    # Sort the list of numbers
    sorted_numbers = sorted(numbers)
    
    # Iterate over the sorted list of numbers
    for i in range(1, len(sorted_numbers)):
        # Check if the current number and the previous number are closer than the threshold
        if sorted_numbers[i] - sorted_numbers[i - 1] < threshold:
            # If they are, return True
            return True
    
    # If no two numbers are closer than the threshold, return False
    return False

# Test cases
print(has_close_elements([1.0, 2.0, 3.0], 0.5))  # False
print(has_close_elements([1.0, 2.8, 3.0, 4.0, 5.0, 2.0], 0.3))  # True
```

This script defines a function `has_close_elements` that takes a list of numbers and a threshold as input. It sorts the list of numbers and then iterates over the sorted list to check if any two numbers are closer than the threshold. If it finds two numbers that are closer than the threshold, it returns `True`. If it doesn't find any two numbers that are closer than the threshold, it returns `False`.

The script includes two test cases to demonstrate the function's behavior. The first test case checks that the function returns `False` when the threshold is greater than the differences between all pairs of numbers. The second test case checks that the function returns `True` when there are two numbers that are closer than the threshold.