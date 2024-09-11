Here is a self-contained Python script that solves the problem in a markdown code block:
```markdown
### has_close_elements Function

This function checks if in a given list of numbers, any two numbers are closer to each other than a given threshold.

#### Code

```python
from typing import List

def has_close_elements(numbers: List[float], threshold: float) -> bool:
    """
    Check if in given list of numbers, are any two numbers closer to each other than given threshold.

    Args:
    numbers (List[float]): List of numbers to check.
    threshold (float): Minimum distance between two numbers to be considered close.

    Returns:
    bool: True if any two numbers are closer to each other than threshold, False otherwise.
    """
    # Sort the list of numbers
    sorted_numbers = sorted(numbers)

    # Iterate over the sorted list, checking each pair of adjacent numbers
    for i in range(1, len(sorted_numbers)):
        # If the distance between two adjacent numbers is less than the threshold, return True
        if sorted_numbers[i] - sorted_numbers[i-1] < threshold:
            return True

    # If no adjacent numbers are closer than the threshold, return False
    return False

#### Example Use Cases

# Test case 1: numbers are not close
print(has_close_elements([1.0, 2.0, 3.0], 0.5))  # Output: False

# Test case 2: numbers are close
print(has_close_elements([1.0, 2.8, 3.0, 4.0, 5.0, 2.0], 0.3))  # Output: True
```

#### Explanation

This function works by first sorting the list of numbers. Then, it iterates over the sorted list, checking each pair of adjacent numbers. If the distance between two adjacent numbers is less than the threshold, it immediately returns True. If it checks all pairs of adjacent numbers without finding any that are closer than the threshold, it returns False.