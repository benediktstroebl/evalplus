```python
from typing import List
import itertools

def has_close_elements(numbers: List[float], threshold: float) -> bool:
    """
    Check if in given list of numbers, are any two numbers closer to each other than
    given threshold.

    Args:
        numbers (List[float]): A list of floating point numbers.
        threshold (float): The minimum distance between two numbers.

    Returns:
        bool: True if two numbers are closer than the threshold, False otherwise.
    """
    # Generate all possible pairs of numbers in the list
    pairs = list(itertools.combinations(numbers, 2))
    
    # Check the distance between each pair of numbers
    for pair in pairs:
        # If the distance between a pair of numbers is less than or equal to the threshold, return True
        if abs(pair[0] - pair[1]) <= threshold:
            return True
    
    # If no pair of numbers is closer than the threshold, return False
    return False

# Test the function
print(has_close_elements([1.0, 2.0, 3.0], 0.5))  # False
print(has_close_elements([1.0, 2.8, 3.0, 4.0, 5.0, 2.0], 0.3))  # True
```

In this script, we use the `itertools.combinations` function to generate all possible pairs of numbers in the input list. Then we iterate over each pair and check the distance between the two numbers. If the distance is less than or equal to the threshold, we return `True`. If no pair of numbers is closer than the threshold, we return `False`.