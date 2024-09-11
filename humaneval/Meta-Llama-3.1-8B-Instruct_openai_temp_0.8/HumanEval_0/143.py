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
        bool: True if any two numbers are closer than the threshold, False otherwise.
    """
    # Generate all pairs of numbers
    pairs = itertools.combinations(enumerate(numbers), 2)
    
    # Check each pair if its distance is less than the threshold
    for (i, _), (j, _) in pairs:
        if abs(numbers[i] - numbers[j]) < threshold:
            return True
    
    return False

# Example usage:
print(has_close_elements([1.0, 2.0, 3.0], 0.5))  # False
print(has_close_elements([1.0, 2.8, 3.0, 4.0, 5.0, 2.0], 0.3))  # True
```

This script uses the `itertools.combinations` function to generate all pairs of numbers from the input list, and then checks each pair to see if its distance is less than the threshold. If it finds a pair that is closer than the threshold, it immediately returns `True`. If it checks all pairs without finding one that is closer than the threshold, it returns `False`.