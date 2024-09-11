```python
from typing import List
import itertools


def has_close_elements(numbers: List[float], threshold: float) -> bool:
    """
    Check if in given list of numbers, are any two numbers closer to each other than given threshold.

    Args:
        numbers (List[float]): A list of numbers.
        threshold (float): The minimum distance between two numbers to be considered close.

    Returns:
        bool: True if any two numbers are closer than the threshold, False otherwise.
    """
    # Generate all pairs of numbers in the list
    pairs = itertools.combinations(numbers, 2)
    
    # Check each pair to see if they are closer than the threshold
    for pair in pairs:
        if abs(pair[0] - pair[1]) <= threshold:
            return True
    
    # If no pairs are closer than the threshold, return False
    return False


# Test the function
if __name__ == "__main__":
    print(has_close_elements([1.0, 2.0, 3.0], 0.5))  # False
    print(has_close_elements([1.0, 2.8, 3.0, 4.0, 5.0, 2.0], 0.3))  # True
```

This script defines a function `has_close_elements` that takes a list of numbers and a threshold as input, and returns `True` if any two numbers in the list are closer than the threshold, and `False` otherwise. It uses the `itertools.combinations` function to generate all pairs of numbers in the list, and then checks each pair to see if they are closer than the threshold. If any pair is closer, it immediately returns `True`. If it checks all pairs without finding any that are closer, it returns `False`. The script also includes test cases to demonstrate the function's behavior.