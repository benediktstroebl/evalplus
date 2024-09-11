```python
from typing import List
import itertools

def has_close_elements(numbers: List[float], threshold: float) -> bool:
    """
    Check if in given list of numbers, are any two numbers closer to each other than given threshold.

    Args:
        numbers (List[float]): The list of numbers to check.
        threshold (float): The minimum distance between two numbers to be considered close.

    Returns:
        bool: True if any two numbers are closer than the threshold, False otherwise.
    """
    # Generate all pairs of numbers in the list
    pairs = list(itertools.combinations(numbers, 2))
    
    # Check each pair to see if they are closer than the threshold
    for pair in pairs:
        if abs(pair[0] - pair[1]) <= threshold:
            return True
    
    # If no pairs are closer than the threshold, return False
    return False

# Example use cases
print(has_close_elements([1.0, 2.0, 3.0], 0.5))  # False
print(has_close_elements([1.0, 2.8, 3.0, 4.0, 5.0, 2.0], 0.3))  # True
print(has_close_elements([10.0, 20.0, 30.0], 10.0))  # False
```

This script defines the `has_close_elements` function, which uses the `itertools.combinations` function to generate all pairs of numbers in the input list. It then checks each pair to see if they are closer than the specified threshold. If any pair is closer than the threshold, the function immediately returns `True`. If no pairs are closer than the threshold, the function returns `False`. The script also includes example use cases to demonstrate how to use the function.