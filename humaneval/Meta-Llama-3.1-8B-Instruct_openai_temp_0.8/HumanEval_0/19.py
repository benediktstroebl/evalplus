### Check for Close Elements in a List of Numbers
```python
from typing import List
import itertools

def has_close_elements(numbers: List[float], threshold: float) -> bool:
    """
    Check if in given list of numbers, are any two numbers closer to each other than given threshold.

    Args:
        numbers (List[float]): A list of floating point numbers.
        threshold (float): The minimum difference between two numbers to be considered close.

    Returns:
        bool: True if any two numbers are closer than the threshold, False otherwise.
    """
    # Generate all pairs of numbers in the list
    pairs = list(itertools.combinations(numbers, 2))
    
    # Check if any pair of numbers has a difference less than or equal to the threshold
    for pair in pairs:
        if abs(pair[0] - pair[1]) <= threshold:
            return True
    
    # If no pair of numbers is closer than the threshold, return False
    return False

# Example usage:
print(has_close_elements([1.0, 2.0, 3.0], 0.5))  # False
print(has_close_elements([1.0, 2.8, 3.0, 4.0, 5.0, 2.0], 0.3))  # True
```
This script uses the `itertools.combinations` function to generate all pairs of numbers in the list, and then checks if any pair has a difference less than or equal to the threshold. If such a pair is found, the function immediately returns `True`. If no such pair is found after checking all pairs, the function returns `False`.