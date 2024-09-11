```python
from typing import List
import itertools

def has_close_elements(numbers: List[float], threshold: float) -> bool:
    """
    Check if in given list of numbers, are any two numbers closer to each other than given threshold.

    Args:
        numbers (List[float]): A list of floating point numbers.
        threshold (float): The minimum distance between two numbers to be considered far enough.

    Returns:
        bool: True if any two numbers are closer than threshold, False otherwise.
    """
    # Use itertools.combinations to get all pairs of numbers
    for num1, num2 in itertools.combinations(numbers, 2):
        # Check if the difference between the two numbers is less than the threshold
        if abs(num1 - num2) < threshold:
            # If a pair with a small difference is found, return True
            return True
    # If no such pair is found after checking all combinations, return False
    return False

# Test the function
print(has_close_elements([1.0, 2.0, 3.0], 0.5))  # False
print(has_close_elements([1.0, 2.8, 3.0, 4.0, 5.0, 2.0], 0.3))  # True
```

This script uses the `itertools.combinations` function to generate all pairs of numbers in the input list. It then checks each pair to see if the difference between the two numbers is less than the threshold. If it finds a pair with a small difference, it immediately returns `True`. If it checks all pairs without finding one, it returns `False`.