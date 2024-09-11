```python
from typing import List
import itertools

def has_close_elements(numbers: List[float], threshold: float) -> bool:
    """
    Check if in given list of numbers, are any two numbers closer to each other than
    given threshold.

    Args:
        numbers: A list of float numbers.
        threshold: The minimum distance between two numbers.

    Returns:
        True if any two numbers are closer than the threshold, False otherwise.
    """
    # Generate all pairs of numbers
    pairs = itertools.combinations(numbers, 2)
    
    # Check if the difference between any pair of numbers is less than the threshold
    for pair in pairs:
        if abs(pair[0] - pair[1]) < threshold:
            # If a pair with a difference less than the threshold is found, return True
            return True
    
    # If no pairs with a difference less than the threshold are found, return False
    return False


# Example use cases
print(has_close_elements([1.0, 2.0, 3.0], 0.5))  # False
print(has_close_elements([1.0, 2.8, 3.0, 4.0, 5.0, 2.0], 0.3))  # True
```

This script uses the `itertools.combinations` function to generate all pairs of numbers in the input list, and then checks if the difference between any pair of numbers is less than the given threshold. If such a pair is found, the function returns `True`; otherwise, it returns `False`.