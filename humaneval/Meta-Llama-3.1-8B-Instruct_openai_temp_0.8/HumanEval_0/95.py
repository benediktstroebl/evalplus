```markdown
### Close Elements Checker

#### Problem Statement
Check if in a given list of numbers, any two numbers are closer to each other than a given threshold.

#### Solution

```python
from typing import List

def has_close_elements(numbers: List[float], threshold: float) -> bool:
    """
    Check if in given list of numbers, are any two numbers closer to each other than given threshold.

    Args:
    numbers (List[float]): List of floating point numbers
    threshold (float): The minimum distance between two numbers to be considered as close

    Returns:
    bool: True if at least two numbers in the list are closer than the threshold, False otherwise
    """
    # Sort the list of numbers
    sorted_numbers = sorted(numbers)
    
    # Iterate over the sorted list to check for close elements
    for i in range(1, len(sorted_numbers)):
        # Check if the difference between current and previous number is less than the threshold
        if sorted_numbers[i] - sorted_numbers[i - 1] < threshold:
            return True
    
    # If no close elements found, return False
    return False

# Example usage
print(has_close_elements([1.0, 2.0, 3.0], 0.5))  # False
print(has_close_elements([1.0, 2.8, 3.0, 4.0, 5.0, 2.0], 0.3))  # True
```
```