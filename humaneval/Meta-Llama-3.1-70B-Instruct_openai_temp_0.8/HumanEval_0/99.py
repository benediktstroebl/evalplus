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
    bool: True if any two numbers are closer than the threshold, False otherwise.
    """
    # Generate all possible pairs of numbers in the list
    pairs = list(itertools.combinations(numbers, 2))

    # Check the distance between each pair of numbers
    for pair in pairs:
        # If the distance between a pair of numbers is less than or equal to the threshold, return True
        if abs(pair[0] - pair[1]) <= threshold:
            return True

    # If no pairs of numbers are closer than the threshold, return False
    return False

# Test cases
print(has_close_elements([1.0, 2.0, 3.0], 0.5))  # False
print(has_close_elements([1.0, 2.8, 3.0, 4.0, 5.0, 2.0], 0.3))  # True
```
This script defines the `has_close_elements` function, which takes a list of numbers and a threshold as input, and returns a boolean indicating whether any two numbers in the list are closer than the threshold.

The function uses the `itertools.combinations` function to generate all possible pairs of numbers in the list, and then checks the distance between each pair of numbers. If the distance between any pair of numbers is less than or equal to the threshold, the function returns `True`. If no pairs of numbers are closer than the threshold, the function returns `False`.

The script also includes two test cases to demonstrate the function's behavior.