```python
from typing import List
import itertools

def has_close_elements(numbers: List[float], threshold: float) -> bool:
    """
    Check if in given list of numbers, are any two numbers closer to each other than
    given threshold.

    Args:
        numbers (List[float]): A list of floating point numbers.
        threshold (float): The maximum allowed distance between two numbers.

    Returns:
        bool: True if any two numbers are closer than the threshold, False otherwise.
    """
    # Generate all possible pairs of numbers
    pairs = list(itertools.combinations(numbers, 2))

    # Check the distance between each pair of numbers
    for pair in pairs:
        # If the distance between any pair is less than the threshold, return True
        if abs(pair[0] - pair[1]) < threshold:
            return True

    # If no pair is closer than the threshold, return False
    return False


# Test cases
print(has_close_elements([1.0, 2.0, 3.0], 0.5))  # False
print(has_close_elements([1.0, 2.8, 3.0, 4.0, 5.0, 2.0], 0.3))  # True
```

Alternatively, you could use the `min` function with a generator expression to simplify the code:

```python
from typing import List
import itertools

def has_close_elements(numbers: List[float], threshold: float) -> bool:
    """
    Check if in given list of numbers, are any two numbers closer to each other than
    given threshold.

    Args:
        numbers (List[float]): A list of floating point numbers.
        threshold (float): The maximum allowed distance between two numbers.

    Returns:
        bool: True if any two numbers are closer than the threshold, False otherwise.
    """
    # Generate all possible pairs of numbers and check the minimum distance
    return min(abs(x - y) for x, y in itertools.combinations(numbers, 2)) < threshold


# Test cases
print(has_close_elements([1.0, 2.0, 3.0], 0.5))  # False
print(has_close_elements([1.0, 2.8, 3.0, 4.0, 5.0, 2.0], 0.3))  # True
```

This version of the function uses the `min` function to find the minimum distance between any two numbers in the list, and then checks if this minimum distance is less than the threshold.