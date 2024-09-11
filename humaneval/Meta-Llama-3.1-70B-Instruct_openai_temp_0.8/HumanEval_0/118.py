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
    # Generate all possible pairs of numbers
    pairs = list(itertools.combinations(enumerate(numbers), 2))

    # Check if the distance between any two numbers is less than the threshold
    for (i, num1), (j, num2) in pairs:
        if abs(num1 - num2) < threshold:
            return True

    return False

# Test cases
print(has_close_elements([1.0, 2.0, 3.0], 0.5))  # False
print(has_close_elements([1.0, 2.8, 3.0, 4.0, 5.0, 2.0], 0.3))  # True
```

This script defines a function `has_close_elements` that takes a list of numbers and a threshold as input, and returns `True` if any two numbers in the list are closer than the threshold, and `False` otherwise.

The function uses the `itertools.combinations` function to generate all possible pairs of numbers in the list. It then checks the distance between each pair of numbers, and returns `True` as soon as it finds a pair with a distance less than the threshold.

If no such pair is found after checking all pairs, the function returns `False`.

The script also includes two test cases to demonstrate the function's behavior.