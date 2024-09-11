```python
from typing import List
import itertools

def has_close_elements(numbers: List[float], threshold: float) -> bool:
    """
    Check if in given list of numbers, are any two numbers closer to each other than
    given threshold.

    Args:
    numbers (List[float]): A list of floating point numbers.
    threshold (float): The minimum distance between two numbers to be considered close.

    Returns:
    bool: True if any two numbers in the list are closer than the threshold, False otherwise.
    """
    # Generate all possible pairs of numbers in the list
    pairs = list(itertools.combinations(numbers, 2))

    # Check each pair to see if the difference between them is less than the threshold
    for pair in pairs:
        if abs(pair[0] - pair[1]) < threshold:
            return True

    # If no pairs were closer than the threshold, return False
    return False


# Test cases
print(has_close_elements([1.0, 2.0, 3.0], 0.5))  # False
print(has_close_elements([1.0, 2.8, 3.0, 4.0, 5.0, 2.0], 0.3))  # True
```

Alternatively, you can use the `min` function with a generator expression to make the function more concise:

```python
from typing import List
import itertools

def has_close_elements(numbers: List[float], threshold: float) -> bool:
    """
    Check if in given list of numbers, are any two numbers closer to each other than
    given threshold.

    Args:
    numbers (List[float]): A list of floating point numbers.
    threshold (float): The minimum distance between two numbers to be considered close.

    Returns:
    bool: True if any two numbers in the list are closer than the threshold, False otherwise.
    """
    # Generate all possible pairs of numbers in the list and check if any are closer than the threshold
    return any(abs(pair[0] - pair[1]) < threshold for pair in itertools.combinations(numbers, 2))


# Test cases
print(has_close_elements([1.0, 2.0, 3.0], 0.5))  # False
print(has_close_elements([1.0, 2.8, 3.0, 4.0, 5.0, 2.0], 0.3))  # True
```