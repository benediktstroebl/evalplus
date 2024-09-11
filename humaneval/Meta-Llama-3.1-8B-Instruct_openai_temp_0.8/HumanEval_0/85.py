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
        bool: True if any two numbers are closer than the threshold, False otherwise.
    """
    # Generate all pairs of numbers
    pairs = list(itertools.combinations(numbers, 2))
    
    # Check if any pair of numbers is closer than the threshold
    for pair in pairs:
        if abs(pair[0] - pair[1]) < threshold:
            return True
    
    # If no pair is closer than the threshold, return False
    return False

# Test cases
if __name__ == "__main__":
    print(has_close_elements([1.0, 2.0, 3.0], 0.5))  # False
    print(has_close_elements([1.0, 2.8, 3.0, 4.0, 5.0, 2.0], 0.3))  # True
```

This script defines a function `has_close_elements` that checks if any two numbers in the given list are closer than the specified threshold. It uses the `itertools.combinations` function to generate all pairs of numbers, and then checks if any pair is closer than the threshold. If such a pair is found, the function returns `True`. If no such pair is found after checking all pairs, the function returns `False`. The test cases at the end of the script demonstrate the function's behavior with different inputs.