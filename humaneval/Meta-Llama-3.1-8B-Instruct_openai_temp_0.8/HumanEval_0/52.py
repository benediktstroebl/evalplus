```python
from typing import List
import itertools

def has_close_elements(numbers: List[float], threshold: float) -> bool:
    """
    Check if in given list of numbers, are any two numbers closer to each other than given threshold.

    Args:
    numbers (List[float]): A list of floating point numbers.
    threshold (float): The minimum distance between two numbers to be considered "close".

    Returns:
    bool: True if there are two numbers closer to each other than the threshold, False otherwise.
    """
    # Generate all possible pairs of numbers
    pairs = itertools.combinations(numbers, 2)
    
    # Check if the difference of any pair of numbers is less than the threshold
    for num1, num2 in pairs:
        if abs(num1 - num2) < threshold:
            return True
    
    # If no pair of numbers is found to be closer than the threshold, return False
    return False

# Example usage:
print(has_close_elements([1.0, 2.0, 3.0], 0.5))  # False
print(has_close_elements([1.0, 2.8, 3.0, 4.0, 5.0, 2.0], 0.3))  # True
```

This script uses the `itertools.combinations` function to generate all possible pairs of numbers in the list, and then checks if the difference of any pair is less than the threshold. The `abs` function is used to calculate the absolute difference between two numbers, which handles both positive and negative differences.