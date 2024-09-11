```python
from typing import List
import itertools

def has_close_elements(numbers: List[float], threshold: float) -> bool:
    """
    Check if in given list of numbers, are any two numbers closer to each other than given threshold.

    Args:
    numbers (List[float]): A list of floating point numbers.
    threshold (float): The minimum distance between two numbers to be considered close.

    Returns:
    bool: True if there are two numbers closer than the threshold, False otherwise.
    """
    # Generate all pairs of numbers in the list
    pairs = list(itertools.combinations(numbers, 2))
    
    # Check each pair to see if the difference is less than the threshold
    for pair in pairs:
        if abs(pair[0] - pair[1]) < threshold:
            return True
    
    # If no pairs were found to be close, return False
    return False

# Example usage:
print(has_close_elements([1.0, 2.0, 3.0], 0.5))  # False
print(has_close_elements([1.0, 2.8, 3.0, 4.0, 5.0, 2.0], 0.3))  # True
```

This script uses the `itertools.combinations` function to generate all pairs of numbers in the list, then checks each pair to see if the difference is less than the threshold. If any pair is found to be close, the function immediately returns `True`. If no pairs are found to be close after checking all of them, the function returns `False`.