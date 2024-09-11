```python
from typing import List
import itertools

def has_close_elements(numbers: List[float], threshold: float) -> bool:
    """
    Check if in given list of numbers, are any two numbers closer to each other than given threshold.

    Args:
        numbers (List[float]): A list of floating point numbers.
        threshold (float): The minimum distance between two numbers.

    Returns:
        bool: True if two numbers are closer than the threshold, False otherwise.
    """
    # Generate all possible pairs of numbers
    pairs = list(itertools.combinations(numbers, 2))
    
    # Check if any pair's difference is less than the threshold
    for pair in pairs:
        if abs(pair[0] - pair[1]) < threshold:
            return True
    
    # If no pair's difference is less than the threshold, return False
    return False

# Test cases
print(has_close_elements([1.0, 2.0, 3.0], 0.5))  # False
print(has_close_elements([1.0, 2.8, 3.0, 4.0, 5.0, 2.0], 0.3))  # True
```

This script uses the `itertools.combinations` function to generate all possible pairs of numbers in the list. It then checks if the absolute difference between any pair of numbers is less than the given threshold. If such a pair is found, the function immediately returns `True`. If no such pair is found after checking all pairs, the function returns `False`.