```markdown
### Close Elements Checker

#### Problem Description
Check if in a given list of numbers, any two numbers are closer to each other than a given threshold.

#### Solution

```python
from typing import List

def has_close_elements(numbers: List[float], threshold: float) -> bool:
    """
    Check if in given list of numbers, are any two numbers closer to each other than given threshold.

    Args:
    numbers (List[float]): List of floating point numbers.
    threshold (float): The minimum distance between two numbers to consider them as close.

    Returns:
    bool: True if any two numbers are closer than the threshold, False otherwise.
    """
    numbers.sort()  # Sort the list to ensure the closest numbers are adjacent
    for i in range(1, len(numbers)):  # Iterate through the list, starting from the second element
        if numbers[i] - numbers[i-1] <= threshold:  # Check if the current element is closer than the threshold to the previous one
            return True
    return False  # If no close elements are found, return False

# Example usage:
print(has_close_elements([1.0, 2.0, 3.0], 0.5))  # False
print(has_close_elements([1.0, 2.8, 3.0, 4.0, 5.0, 2.0], 0.3))  # True
```

This script defines a function `has_close_elements` that takes a list of numbers and a threshold as input. It sorts the list, then iterates through it, checking if each element is closer to its predecessor than the given threshold. If it finds any two elements that meet this condition, it returns `True`. If no such elements are found after checking all pairs, it returns `False`.