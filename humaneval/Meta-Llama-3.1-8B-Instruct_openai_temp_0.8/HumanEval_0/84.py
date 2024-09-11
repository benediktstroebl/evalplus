### Solution to Problem
```markdown
## has_close_elements.py

### Check if in given list of numbers, are any two numbers closer to each other than given threshold.

```python
from typing import List

def has_close_elements(numbers: List[float], threshold: float) -> bool:
    """
    Check if in given list of numbers, are any two numbers closer to each other than given threshold.

    Args:
        numbers (List[float]): A list of floating point numbers.
        threshold (float): The minimum distance between two numbers to be considered close.

    Returns:
        bool: True if any two numbers in the list are closer than the given threshold, False otherwise.

    >>> has_close_elements([1.0, 2.0, 3.0], 0.5)
    False
    >>> has_close_elements([1.0, 2.8, 3.0, 4.0, 5.0, 2.0], 0.3)
    True
    """
    numbers.sort()  # Sort the list to allow for efficient comparison
    for i in range(1, len(numbers)):
        # Check if the difference between two adjacent numbers is less than the threshold
        if numbers[i] - numbers[i-1] < threshold:
            return True
    return False

# Example usage:
print(has_close_elements([1.0, 2.0, 3.0], 0.5))  # False
print(has_close_elements([1.0, 2.8, 3.0, 4.0, 5.0, 2.0], 0.3))  # True
```
This script defines a function `has_close_elements` that takes a list of floating point numbers and a threshold value. It sorts the list to allow for efficient comparison and then iterates over the sorted list to check if any two adjacent numbers are closer than the threshold. If such a pair is found, the function immediately returns `True`. If no such pair is found after iterating over the entire list, the function returns `False`.